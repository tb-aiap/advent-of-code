"""Solution for Day 15 2024."""

import pprint

from utils import Direction, get_data


def check_in_front(curr_pos: tuple[int], curr_dir: Direction):

    r, c = curr_pos
    row_dir, col_dir = curr_dir.value
    next_row, next_col = r + row_dir, c + col_dir

    return next_row, next_col


def get_guard_pos(grid):
    guard_pos = [(idx, i.index("@")) for idx, i in enumerate(grid) if "@" in i][0]
    return guard_pos


def move_in_front(curr_pos: tuple[int], curr_dir: Direction, grid: list[list[str]]):

    r, c = curr_pos[0], curr_pos[1]
    stack = [(r, c)]
    while stack and grid[r][c] != "#":
        r, c = check_in_front((r, c), curr_dir)

        if grid[r][c] == ".":
            while stack:
                sr, sc = stack.pop()
                grid[r][c] = grid[sr][sc]
                grid[sr][sc] = "."
                r, c = sr, sc
        else:
            stack.append((r, c))

    return grid


def main(data):
    grid = [[j for j in i] for i in data[: data.index("")]]
    moves = "".join(data[data.index("") + 1 :])

    guard_pos = [(idx, i.index("@")) for idx, i in enumerate(grid) if "@" in i][0]

    for d in moves:
        if d == "^":
            dir = Direction.UP
            grid = move_in_front(guard_pos, dir, grid)
            guard_pos = get_guard_pos(grid)
        elif d == "v":
            dir = Direction.DOWN
            grid = move_in_front(guard_pos, dir, grid)
            guard_pos = get_guard_pos(grid)
        elif d == "<":
            dir = Direction.LEFT
            grid = move_in_front(guard_pos, dir, grid)
            guard_pos = get_guard_pos(grid)
        elif d == ">":
            dir = Direction.RIGHT
            grid = move_in_front(guard_pos, dir, grid)
            guard_pos = get_guard_pos(grid)

    part_1 = 0
    for ridx, r in enumerate(grid):
        for cidx, c in enumerate(grid[ridx]):
            if grid[ridx][cidx] == "O":
                part_1 += (100 * ridx) + cidx
    part_2 = 0
    return part_1, part_2


if __name__ == "__main__":

    data = get_data(15)
    part_1, part_2 = main(data)

    print("Solution for Part 1", part_1)
    print("Solution for Part 2", part_2)
