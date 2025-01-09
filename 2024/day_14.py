"""Solution for Day 14 2024."""

from collections import defaultdict
from functools import reduce
from operator import mul

import matplotlib.pyplot as plt

from utils import get_data, timer

WIDTH = 101
HEIGHT = 103
GRID = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]  # for with function


def parse_row_col(val: str, key: str):
    col, row = val.lstrip(key).split(",")
    return int(row), int(col)


def update_pos(pos, vel, time, grid):

    pr, pc = pos
    vr, vc = vel

    nr, nc = pr + (time * vr), pc + (time * vc)
    return nr % len(grid), nc % len(grid[0])


def assign_quadrant(pos: tuple[int, int], grid: list[list[int]]):

    row_up, row_down = len(grid) // 2 - 1, len(grid) // 2 + 1
    col_left, col_right = len(grid[0]) // 2 - 1, len(grid[0]) // 2 + 1

    r, c = pos
    if r <= row_up and c <= col_left:
        return "1"
    if r <= row_up and c >= col_right:
        return "2"
    if r >= row_down and c <= col_left:
        return "3"
    if r >= row_down and c >= col_right:
        return "4"


@timer
def main(data):

    pos = [parse_row_col(pos.split(" ")[0], key="p=") for pos in data]
    vel = [parse_row_col(pos.split(" ")[1], key="v=") for pos in data]
    result = defaultdict(int)

    # part 1
    time_sec = 100
    new_pos = [update_pos(p, v, time_sec, GRID) for p, v in zip(pos, vel)]

    for p in new_pos:
        q = assign_quadrant(p, GRID)
        if q:
            result[q] += 1

    part_1 = reduce(mul, result.values())

    # part 2 - visual inspect
    time_sec = 7
    for _ in range(100):
        new_pos = []
        for p, v in zip(pos, vel):
            new_pos.append(update_pos(p, v, time_sec, GRID))

        plt.scatter(
            [p[1] for p in new_pos],
            [p[0] for p in new_pos],
        )
        plt.title(f"Iteration {_}")
        plt.savefig(f"{time_sec}.png")
        plt.close()
        time_sec += 101

    return part_1


if __name__ == "__main__":

    data = get_data(14)
    part_1 = main(data)
