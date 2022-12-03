use std::{collections::HashMap, fs};

fn calculate_outcome_score(enemy_play: &str, my_play: &str) -> u32 {
    let rock_map: HashMap<&str, u32> = HashMap::from([("Y", 6), ("X", 3), ("Z", 0)]);
    let paper_map: HashMap<&str, u32> = HashMap::from([("Y", 3), ("X", 0), ("Z", 6)]);
    let scissors_map: HashMap<&str, u32> = HashMap::from([("Y", 0), ("X", 6), ("Z", 3)]);
    let win_map: HashMap<&str, HashMap<&str, u32>> =
        HashMap::from([("A", rock_map), ("B", paper_map), ("C", scissors_map)]);

    return win_map[enemy_play][my_play];
}

fn calculate_score(enemy_play: &str, my_play: &str) -> u32 {
    let outcome_score = calculate_outcome_score(enemy_play, my_play);

    let scape_score_map: HashMap<&str, u32> = HashMap::from([("Y", 2), ("X", 1), ("Z", 3)]);
    let shape_score = scape_score_map[my_play];

    return outcome_score + shape_score;
}

fn parse_score(line: &str) -> (&str, &str) {
    let inputs = line.split(" ").collect::<Vec<&str>>();
    return (inputs[0], inputs[1]);
}

fn main() {
    let contents = fs::read_to_string("./input.txt").expect("Should read input file");

    let mut total_score: u32 = 0;
    contents.split("\n").for_each(|line| {
        if line.len() == 0 {
            return;
        }

        let (enemy_play, my_play) = parse_score(line);
        total_score += calculate_score(enemy_play, my_play);
    });

    println!("{}", total_score)
}
