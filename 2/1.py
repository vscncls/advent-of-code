from dataclasses import dataclass
from collections import Counter

@dataclass
class FrequencyRange:
    min: int
    max: int

@dataclass
class Input:
    frequency_range: FrequencyRange
    leter_rule: str
    password: str

def get_input() -> list[Input]:
    raw_data = None
    with open("./input.txt", "r") as file:
        raw_data = file.read()
    raw_data_by_line = raw_data.split('\n')
    raw_data_by_line_separated = [line.split(' ') for line in raw_data_by_line if len(line) > 0]

    result = []
    for line in raw_data_by_line_separated:
        range_ = line[0].split('-')
        frequency = FrequencyRange(int(range_[0]), int(range_[1]))
        result.append(Input(frequency, line[1].replace(':', ''), line[2]))

    return result

def input_is_valid(entry: Input) -> bool:
    frequency = Counter(entry.password)[entry.leter_rule]
    return entry.frequency_range.min <= frequency <= entry.frequency_range.max

def count_valid_inputs(inputs: list[Input]) -> int:
    total = 0
    for input in inputs:
        if input_is_valid(input):
            total += 1

    return total

if __name__ == "__main__":
    inputs = get_input()
    total_valid = count_valid_inputs(inputs)
    print(f"Total valid inputs: {total_valid}")

