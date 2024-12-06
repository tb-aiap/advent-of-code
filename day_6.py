from enum import Enum

from utils import get_data

DAY = 6


class Direction(Enum):
    # row, col
    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)


TURN_RIGHT = {
    "UP": "RIGHT",
    "DOWN": "LEFT",
    "LEFT": "UP",
    "RIGHT": "DOWN",
}

OBSTACLE = "#"


def get_guard_position(map_arr: list[int]):

    for idx, r in enumerate(map_arr):
        if "^" in r:
            return idx, r.index("^")

    return ValueError("There is no ^ in the map")


def check_in_front(curr_pos: tuple[int], curr_dir: Direction):

    crow, ccol = curr_pos
    row_dir, col_dir = curr_dir.value
    next_row, next_col = crow + row_dir, ccol + col_dir

    return next_row, next_col


def main(data):

    curr_pos = get_guard_position(data)
    data[curr_pos[0]] = data[curr_pos[0]].replace("^", ".")

    curr_dir = Direction.UP
    path_taken = {curr_pos}  # INCLUDING THE GUARD STARTING POSITION!!!!!!

    while True:

        nr, nc = check_in_front(curr_pos, curr_dir)
        if 0 > nr or nr >= len(data) or 0 > nc or nc >= len(data[0]):
            break

        elif data[nr][nc] == ".":
            # move same dir
            curr_pos = (nr, nc)
            path_taken.add(curr_pos)

        elif data[nr][nc] == OBSTACLE:
            # turn right
            curr_dir = Direction[TURN_RIGHT[curr_dir.name]]

    part_1 = len(path_taken)
    return part_1, 0


if __name__ == "__main__":

    data = get_data(6)
    part_1, part_2 = main(data)

    print("Solution for Part 1", part_1)
    print("Solution for Part 2", part_2)
