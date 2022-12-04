use std::{convert::TryInto, fs};

fn main() {
    let contents = fs::read_to_string("./input.txt").expect("Should read input file");

    let mut total_score: u32 = 0;
    contents.split("\n").for_each(|line| {
        if line.len() == 0 {
            return;
        }
        let (a_half, b_half) = parse_contents(line);
        let repeated_letter = repeat_letter(a_half, b_half).unwrap();
        let score = score_letter(repeated_letter).unwrap();
        total_score += score;
    });

    println!("{}", total_score);
}

fn parse_contents(line: &str) -> (&str, &str) {
    return line.split_at(line.len() / 2);
}

fn repeat_letter(a: &str, b: &str) -> Result<char, &'static str> {
    // dumb but works
    // should use hashset
    for a_letter in a.chars() {
        if b.contains(a_letter) {
            return Ok(a_letter);
        }
    }

    return Err("common letter not found");
}

const ALPHABET: &str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";

fn score_letter(letter: char) -> Result<u32, &'static str> {
    for (index, alpha_letter) in ALPHABET.chars().enumerate() {
        if letter == alpha_letter {
            let letter_index: u32 = index.try_into().unwrap();
            let score = letter_index + 1;
            return Ok(score);
        }
    }

    return Err("letter not found in alphabet");
}
