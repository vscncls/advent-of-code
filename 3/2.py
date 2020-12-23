from enum import Enum


class Square(Enum):
    TREE = "#"
    OPEN = "."


def get_input() -> list[list[Square]]:
    raw = None
    with open("./input.txt", "r") as file:
        raw = file.read()
    map_ = []
    for line in raw.split("\n"):
        if len(line) == 0:
            continue

        map_line = []
        for symbol in line:
            map_line.append(Square(symbol))

        map_.append(map_line)

    return map_


def get_tree_hits_in_path(map_: list[list[Square]], steps: tuple[int, int]) -> int:
    index = 0
    hits = 0
    for line in map_[0::steps[1]]:
        if line[index] == Square.TREE:
            hits += 1

        index += steps[0]
        index = index % len(line)

    return hits


if __name__ == "__main__":
    map_ = get_input()
    steps_entries = [(1,1), (3,1), (5,1), (7,1), (1,2)]
    hits = [get_tree_hits_in_path(map_, steps_entry) for steps_entry in steps_entries]
    total = 1
    for hit in hits:
        total *= hit
    print(f"Result: {total}")
