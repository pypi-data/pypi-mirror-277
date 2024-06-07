use rustc_hash::FxHashMap;
// use serde_json;
use std::cell::RefCell;
use std::error::Error;
// use std::collections::HashMap;
use std::io::Write;
use std::{fs, str};

// type Map<K, V> = HashMap<K, V>;
type Map<K, V> = FxHashMap<K, V>;
type Rank = u32;

pub trait Tokenizer {
    fn train(&mut self, text: &str, vocab_size: usize) -> Vec<Rank>;
    fn encode(&self, text: &str) -> Vec<Rank>;
    fn decode(&self, _input_ids: &[Rank]) -> String;
}

pub trait Normalize {
    fn normalize(&self, text: &mut String);
}

pub struct DefaultNormalizer {}
impl DefaultNormalizer {
    fn is_whitespace(&self, c: u8) -> bool {
        c == b' ' || c == b'\t'
    }
}
impl Normalize for DefaultNormalizer {
    // https://stackoverflow.com/questions/71864137/whats-the-ideal-way-to-trim-extra-spaces-from-a-string
    fn normalize(&self, text: &mut String) {
        let mut prev = ' ';
        text.retain(|x| {
            let res = !self.is_whitespace(x as u8) || !self.is_whitespace(prev as u8);
            prev = x;
            res
        });
    }
}

pub struct BPETokenizer<T>
where
    T: Normalize,
{
    pub normalizer: T,
    encoder: Map<(Rank, Rank), Rank>, //TODO: make private later
    decoder: RefCell<Option<Map<Rank, (Rank, Rank)>>>,
}

fn _byte_pair_merge(pieces: &mut Vec<Rank>, find: (Rank, Rank), replace: Rank) {
    let mut remove = Vec::new();
    let mut prev: bool = true;
    pieces.windows(2).enumerate().for_each(|(i, x)| {
        if (x[0], x[1]) == find && prev {
            remove.push(i + 1);
            prev = false;
        } else {
            prev = true;
        }
    });

    // println!("{:?}", remove);
    for (j, i) in remove.iter().enumerate() {
        pieces[i - j - 1] = replace;
        pieces.remove(i - j);
    }
}
// fn _byte_pair_merge(pieces: &mut Vec<Rank>, find: (Rank, Rank), replace: Rank) {
//     let mut i = 0;
//     while i < pieces.len() - 1 {
//         if (pieces[i], pieces[i + 1]) == find {
//             pieces[i] = replace;
//             pieces.remove(i + 1);
//         }
//         i += 1;
//     }
// }

// impl BPETokenizer<DefaultNormalizer> {
//     pub fn new() -> Self {
//         Self {
//             normalizer: DefaultNormalizer {},
//             encoder: Map::default(),
//             decoder: RefCell::new(None),
//         }
//     }
// }

impl<T> BPETokenizer<T>
where
    T: Normalize,
{
    pub fn new(normalizer: T) -> Self {
        Self {
            normalizer,
            encoder: Map::default(),
            decoder: RefCell::new(None),
        }
    }

    // pub fn from_pretrained(file: &str) -> Result<Self, Box<dyn Error>> {
    //     let mut tok = Self::new(DefaultNormalizer {});
    //     tok.load_encoder(file)?;
    //     Ok(tok)
    // }

    pub fn preprocess(&self, text: &mut String) {
        self.normalizer.normalize(text);
    }

    pub fn save_encoder(&self, file: &str) -> Result<(), Box<dyn std::error::Error>> {
        // need to reverse key-value order since serde can't serialize tuples as map keys
        let decoder: Map<&Rank, &(Rank, Rank)> = self.encoder.iter().map(|(k, v)| (v, k)).collect();

        let serialized = serde_json::to_string(&decoder)?;
        let mut f = fs::File::create(file)?;

        f.write_all(serialized.as_bytes())?;

        Ok(())
    }

    pub fn load_encoder(&mut self, file: &str) -> Result<(), Box<dyn std::error::Error>> {
        let encoder_str = fs::read_to_string(file)?;
        let _encoder: Map<Rank, (Rank, Rank)> = serde_json::from_str(&encoder_str)?;
        let encoder: Map<(Rank, Rank), Rank> = _encoder.iter().map(|(&k, &v)| (v, k)).collect();

        self.encoder = encoder;
        self.decoder = RefCell::new(Some(_encoder));

        Ok(())
    }

    fn _encode_chunk(&self, chunk: &[u8]) -> Vec<Rank> {
        let mut pieces: Vec<Rank> = chunk.to_vec().iter().map(|&x| x as Rank).collect();

        loop {
            let mut merges = Vec::new();
            for i in 0..pieces.len() - 1 {
                if let Some(&rank) = self.encoder.get(&(pieces[i], pieces[i + 1])) {
                    merges.push((i, rank));
                }
            }
            if merges.is_empty() {
                break;
            }

            // apply merges and swap in tokens from reverse
            let mut i = merges.len() - 1;
            while i > 0 {
                let x = &mut merges[i - 1..=i];
                let l = x[0];
                let r = x[1];

                if r.0 - l.0 > 1 && r.1 != Rank::MAX {
                    pieces[r.0] = r.1;
                    pieces.remove(r.0 + 1);
                } else if r.1 < l.1 {
                    pieces[r.0] = r.1;
                    pieces.remove(r.0 + 1);

                    x[0].1 = Rank::MAX;
                    i -= 1;
                }
                //avoid overflow on usize 0-1
                if i == 0 {
                    break;
                }
                i -= 1;
            }
            if merges.len() == 1 || merges[0].1 < merges[1].1 {
                pieces[merges[0].0] = merges[0].1;
                pieces.remove(merges[0].0 + 1);
            }
        }
        pieces
    }

    fn _decode_chunk(&self, chunk: &[Rank]) -> Vec<u8> {
        let mut pieces: Vec<Rank> = Vec::from(chunk);
        let decoder: Map<Rank, (Rank, Rank)> = match self.decoder.borrow_mut().take() {
            Some(d) => d,
            None => self.encoder.iter().map(|(&k, &v)| (v, k)).collect(),
        };

        loop {
            let mut demerges = Vec::new();
            for i in 0..pieces.len() {
                let rank = pieces[i];
                if let Some(&tup) = decoder.get(&rank) {
                    demerges.push((i, tup));
                }
            }
            // our tokenizer doesn't have by default 0-255 in the encoder
            // so this stops when we're left with u8's only
            if demerges.is_empty() {
                break;
            }

            for op in demerges.iter().rev() {
                let i = op.0;
                let tup = op.1;
                pieces[i] = tup.0;
                pieces.insert(i + 1, tup.1);
            }
        }
        //give back decoder
        *self.decoder.borrow_mut() = Some(decoder);

        pieces.iter().map(|&x| x as u8).collect()
    }
}

impl<T> Tokenizer for BPETokenizer<T>
where
    T: Normalize,
{
    fn train(&mut self, text: &str, vocab_size: usize) -> Vec<Rank> {
        assert!(vocab_size > 0);
        let mut pieces: Vec<Rank>;

        if !self.encoder.is_empty() {
            println!("pretrained tokenizer detected!");
            pieces = self.encode(text);
        } else {
            let text = text.as_bytes();
            pieces = text.iter().map(|&i| i as Rank).collect();
        }

        for _ in tqdm::tqdm(0..vocab_size - self.encoder.len()) {
            let mut counts: Map<(Rank, Rank), Rank> = Map::default();
            for i in 0..pieces.len() - 1 {
                *counts.entry((pieces[i], pieces[i + 1])).or_insert(0) += 1;
            }

            let (&p, _) = counts.iter().max_by_key(|(_, &c)| c).unwrap();
            let token_id = (self.encoder.len() + 1 + 255) as Rank; // need 255 offset since ascii chars occupy 0-255

            self.encoder.insert(p, token_id);
            _byte_pair_merge(&mut pieces, p, token_id);
        }
        pieces
    }

    //TODO: add chunk_size arg or specify in config
    fn encode(&self, text: &str) -> Vec<Rank> {
        let text = text.as_bytes();

        const CHUNK_SIZE: usize = 4 * 4096;

        let mut encoded_chunks = Vec::new();
        let z: usize = (text.len() % CHUNK_SIZE > 0) as usize;
        for i in 0..text.len() / CHUNK_SIZE + z {
            let chunk = &text[CHUNK_SIZE * i..usize::min(CHUNK_SIZE * (i + 1), text.len())];
            // println!("{:?}", str::from_utf8(chunk));
            encoded_chunks.push(self._encode_chunk(chunk));
        }

        encoded_chunks.into_iter().flatten().collect()
    }

    fn decode(&self, _input_ids: &[Rank]) -> String {
        const CHUNK_SIZE: usize = 4096;

        let mut decoded_chunks = Vec::new();
        let z: usize = (_input_ids.len() % CHUNK_SIZE > 0) as usize;
        for i in 0.._input_ids.len() / CHUNK_SIZE + z {
            let chunk =
                &_input_ids[CHUNK_SIZE * i..usize::min(CHUNK_SIZE * (i + 1), _input_ids.len())];
            // println!("{:?}", str::from_utf8(chunk));
            decoded_chunks.push(self._decode_chunk(chunk));
        }

        let utf8: Vec<u8> = decoded_chunks.into_iter().flatten().collect();
        String::from(str::from_utf8(&utf8).unwrap())
    }

    // fn decode(&self, _input_ids: &[Rank]) -> String {
    //     //need to apply merge-outs in reverse order
    //     let decoder: Map<Rank, (Rank, Rank)> = match self.decoder.borrow_mut().take() {
    //         Some(d) => d,
    //         None => self.encoder.iter().map(|(&k, &v)| (v, k)).collect(),
    //     };
    //     let mut input_ids = Vec::from(_input_ids);
    //
    //     for token in (255..256 + self.encoder.len()).rev() {
    //         let token = token as Rank;
    //
    //         let mut i = 0;
    //         while i < input_ids.len() {
    //             if input_ids[i] == token {
    //                 let pair = *decoder.get(&token).unwrap();
    //                 input_ids[i] = pair.0;
    //                 input_ids.insert(i + 1, pair.1);
    //                 i += 1;
    //             }
    //             i += 1;
    //         }
    //     }
    //
    //     //give back decoder
    //     *self.decoder.borrow_mut() = Some(decoder);
    //
    //     let arr_u8: Vec<u8> = input_ids.iter().map(|&x| x as u8).collect();
    //     String::from(str::from_utf8(&arr_u8).unwrap())
    // }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_encode_decode() {
        let mut tok = BPETokenizer::new(DefaultNormalizer {});
        let _ = tok.load_encoder("wikibpe.json");

        let text = String::from("this is an example. 😎");
        assert_eq!(text, tok.decode(&tok.encode(&text)));
    }

    #[test]
    fn test_compression() {
        let mut tok = BPETokenizer::new(DefaultNormalizer {});
        let _ = tok.load_encoder("wikibpe.json");

        let text = String::from("this is an example. 😎");

        assert!(text.len() > tok.encode(&text).len());
    }
}
