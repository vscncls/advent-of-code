def read_file_to_strings() -> list[str]:
    with open("input.txt") as file:
        return file.readlines()


def transform_input(entry: list[str]) -> list[int]:
    result: list[int] = []
    for i in entry:
        result.append(int(i))

    return result


def get_window_depth(depth_list: list[int], start: int, amount: int):
    total = 0
    for i in range(start, start + amount):
        total += depth_list[i]

    return total


def count_number_of_increases(depth_list: list[int]) -> int:
    total = 0
    for index, _ in enumerate(depth_list):
        if (len(depth_list) - 1) < (index + 3):
            break

        current_window_depth = get_window_depth(depth_list, index, 3)
        next_window_depth = get_window_depth(depth_list, index + 1, 3)

        if next_window_depth > current_window_depth:
            total += 1

    return total


if __name__ == "__main__":
    print(count_number_of_increases(transform_input(read_file_to_strings())))
