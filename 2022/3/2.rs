use std::{collections::HashSet, convert::TryInto, fs, vec};

fn main() {
    let contents = fs::read_to_string("./input.txt").expect("Should read input file");

    let groups = parse_contents(&contents);
    let mut total_score: u32 = 0;
    for ele in groups {
        total_score += score_letter(repeat_letter(ele)).unwrap();
    }

    println!("{}", total_score);
}

fn parse_contents(file: &str) -> Vec<Vec<&str>> {
    let mut groups: Vec<Vec<&str>> = vec![];
    let mut current_group: Vec<&str> = vec![];
    let group_size = 3;
    file.split("\n").for_each(|line| {
        if current_group.len() == group_size {
            groups.push(current_group.clone());
            current_group.clear();
        }

        if line.len() == 0 {
            return;
        }

        current_group.push(line);
    });

    return groups;
}

fn repeat_letter(group: Vec<&str>) -> char {
    let mut group_hashets: Vec<HashSet<char>> = vec![];
    for ele in group {
        let mut ele_hashset: HashSet<char> = HashSet::new();
        for letter in ele.chars() {
            ele_hashset.insert(letter.clone());
        }
        group_hashets.push(ele_hashset.clone());
    }

    let mut common = group_hashets.pop().unwrap();
    for ele in group_hashets {
        common = common
            .iter()
            .filter(|it| ele.contains(*it))
            .cloned()
            .collect();
    }

    let repeat_vec: Vec<&char> = common.iter().collect();
    return repeat_vec[0].clone();
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
