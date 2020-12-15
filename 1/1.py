def get_input() -> list[int]:
    numbers_raw = None
    with open("./input.txt", "r") as file:
        numbers_raw = file.read()

    numbers_string = numbers_raw.split("\n")
    numbers = [int(number) for number in numbers_string if str.isnumeric(number)]
    return numbers


def find_matching_sum(numbers: list[int], target: int) -> tuple[int, int]:
    sorted_numbers = sorted(numbers)
    for number_index in range(len(numbers)):
        for potential_match_index in range(number_index, len(numbers)):
            if (
                sorted_numbers[number_index] + sorted_numbers[potential_match_index]
                == target
            ):
                return (
                    sorted_numbers[number_index],
                    sorted_numbers[potential_match_index],
                )

    raise Exception("Match not found.")

TARGET = 2020

if __name__ == "__main__":
    match = find_matching_sum(get_input(), TARGET)
    result = match[0] * match[1]
    print(f"Result: {result}")
