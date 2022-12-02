from enum import Enum

class MoveCommand(Enum):
    FORWARD = "forward"
    DOWN = "down"
    UP = "up"

def move(command: MoveCommand, value: int, curr_pos: tuple[int, int, int]) -> tuple[int, int, int]:
    if command == MoveCommand.FORWARD:
        return curr_pos[0] + value, curr_pos[1] + (curr_pos[2] * value), curr_pos[2]
    elif command ==  MoveCommand.DOWN:
        return curr_pos[0], curr_pos[1], curr_pos[2] + value
    elif command ==  MoveCommand.UP:
        return curr_pos[0], curr_pos[1], curr_pos[2] - value

def read_file_to_strings() -> list[str]:
    with open("input.txt") as file:
        return file.readlines()

def transform_input(entry: list[str]) -> list[tuple[MoveCommand, int]]:
    result: list[tuple[MoveCommand, int]] = []
    for i in entry:
        command = i.split(" ")
        result.append((MoveCommand(command[0]), int(command[1])))

    return result

def calculate_result(entry: list[tuple[MoveCommand, int]]) -> tuple[int, int, int]:
    curr_pos = (0, 0, 0)
    for i in entry:
        curr_pos = move(i[0], i[1], curr_pos)
    return curr_pos

if __name__ == "__main__":
    final_pos = calculate_result(transform_input(read_file_to_strings()))
    print(final_pos)
    print(final_pos[0] * final_pos[1])
