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

    curr_dir = Direction.UP
    path_taken = {curr_pos}  # INCLUDING THE GUARD STARTING POSITION!!!!!!

    while True:

        nr, nc = check_in_front(curr_pos, curr_dir)
        if 0 > nr or nr >= len(data) or 0 > nc or nc >= len(data[0]):
            break

        elif data[nr][nc] in [".", "^"]:
            # move same dir
            curr_pos = (nr, nc)
            path_taken.add(curr_pos)

        elif data[nr][nc] == OBSTACLE:
            # turn right
            curr_dir = Direction[TURN_RIGHT[curr_dir.name]]

    part_1 = len(path_taken)
    return part_1


def main_part_2(data):
    from collections import defaultdict

    curr_pos = get_guard_position(data)

    ## Brute forcing every single potential placement
    path_arr = set()
    for i in range(len(data)):
        for j in range(len(data)):
            if data[i][j] == ".":
                path_arr.add((i, j))
    ## Brute forcing every single potential placement

    curr_dir = Direction.UP
    try_coord = path_arr.pop()
    result = 0
    moved_path = defaultdict(int)

    while True:
        nr, nc = check_in_front(curr_pos, curr_dir)
        if 0 > nr or nr >= len(data) or 0 > nc or nc >= len(data[0]):
            curr_pos = get_guard_position(data)
            curr_dir = Direction.UP
            moved_path = defaultdict(int)
            try:
                try_coord = path_arr.pop()
            except:
                print("Set is empty")
                break
            continue

        elif data[nr][nc] in [".", "^"] and (nr, nc) != (try_coord[0], try_coord[1]):
            # move same dir
            curr_pos = (nr, nc)

        elif data[nr][nc] == OBSTACLE or try_coord == (try_coord[0], try_coord[1]):
            # turn right
            curr_dir = Direction[TURN_RIGHT[curr_dir.name]]
            moved_path[(curr_pos, curr_dir.name)] += 1
            if moved_path[(curr_pos, curr_dir.name)] > 1:
                result += 1
                try:
                    try_coord = path_arr.pop()
                except:
                    print("Set is empty")
                    break
                curr_pos = get_guard_position(data)
                curr_dir = Direction.UP
                del moved_path
                moved_path = defaultdict(int)

    return result


if __name__ == "__main__":

    data = get_data(6)
    part_1 = main(data)
    part_2 = main_part_2(data)

    print("Solution for Part 1", part_1)
    print("Solution for Part 2", part_2)
