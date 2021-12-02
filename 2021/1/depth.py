def read_file_to_strings() -> list[str]:
    with open("input.txt") as file:
        return file.readlines()

def transform_input(entry: list[str]) -> list[int]:
    result: list[int] = []
    for i in entry:
        result.append(int(i))

    return result

def count_number_of_increases(depth_list: list[int]) -> int:
    total = 0
    # We are garanteed to have 1+ itens in the list, so this is fine
    previous_depth = depth_list.pop(0)
    for current_depth in depth_list:
        if current_depth > previous_depth:
            total += 1

        previous_depth = current_depth

    return total


if __name__ == "__main__":
    print(count_number_of_increases(transform_input(read_file_to_strings())))
