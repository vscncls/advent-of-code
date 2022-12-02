use std::fs;

fn main() {
    let contents = fs::read_to_string("./input.txt").expect("Should read input file");

    let mut elfs_calories: Vec<u32> = vec![];

    let mut current_elf_calories: u32 = 0;
    contents.split("\n").for_each(|line| {
        if line == "" {
            elfs_calories.push(current_elf_calories);
            current_elf_calories = 0;
            return;
        }

        let calories = line.parse::<u32>().unwrap();
        current_elf_calories += calories;
    });

    let biggest = elfs_calories.iter().max().unwrap();

    println!("{}", biggest)
}
