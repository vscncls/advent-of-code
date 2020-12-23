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


def get_tree_hits_in_path(map_: list[list[Square]]) -> int:
    index = 0
    hits = 0
    for line in map_:
        print(index)
        if line[index] == Square.TREE:
            hits += 1

        index += 3
        index = index % len(line)

    return hits


if __name__ == "__main__":
    map_ = get_input()
    hits = get_tree_hits_in_path(map_)
    print(f"Times a tree was hit: {hits}")
