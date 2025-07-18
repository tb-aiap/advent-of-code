"""Solution for Day 3 2023."""

from collections import defaultdict
from functools import reduce
from operator import mul

import utils

# for each row, for each number scan 9 diretions for symbol.

scan_direction = [
    # row, col
    (-1, 0),  # up 0
    (-1, 1),  # up right
    (0, 1),  # 0 right
    (1, 1),  # right down
    (1, 0),  # down 0
    (1, -1),  # down left
    (0, -1),  # 0 left
    (-1, -1),  # left up
]


def number_near_parts(data: list[list[str]], r: int, c: int) -> bool:
    """Search surrounding area for parts"""
    for dir in scan_direction:
        dir_r = r + dir[0]
        dir_c = c + dir[1]
        if not (0 <= dir_r < len(data) and 0 <= dir_c < len(data[0])):
            continue  # out of bounds
        if not data[dir_r][dir_c].isnumeric() and data[dir_r][dir_c] != ".":
            # this number is near a part
            return True
    return False


def number_near_gear(data: list[list[str]], r: int, c: int) -> tuple[int]:
    """Search surrounding area for parts"""
    for dir in scan_direction:
        dir_r = r + dir[0]
        dir_c = c + dir[1]
        if not (0 <= dir_r < len(data) and 0 <= dir_c < len(data[0])):
            continue  # out of bounds
        if data[dir_r][dir_c] == "*":
            return dir_r, dir_c
    return -1, -1


def loop_through_chars(data: list[list[str]], part2: bool = False) -> int:
    """Solution for part 1."""
    result = 0
    gear_ratio = defaultdict(list)
    for r in range(len(data)):
        number_holder = ""
        is_near_parts = False
        gear_coord = -1, -1
        for c in range(len(data[r])):
            val = data[r][c]
            if val.isnumeric():
                number_holder += val
                if not is_near_parts:
                    is_near_parts = number_near_parts(data, r, c)
                if part2 and gear_coord == (-1, -1):
                    gear_coord = number_near_gear(data, r, c)
            else:
                if number_holder and is_near_parts:
                    result += int(number_holder)
                    is_near_parts = False
                if part2 and number_holder and gear_coord != (-1, -1):
                    gear_ratio[gear_coord].append(int(number_holder))
                    gear_coord = -1, -1
                number_holder = ""

        if number_holder and is_near_parts:
            result += int(number_holder)
            is_near_parts = False
        if part2 and number_holder and gear_coord != (-1, -1):
            gear_ratio[gear_coord].append(int(number_holder))
            gear_coord = -1, -1

    if part2:
        result = sum(reduce(mul, v, 1) for v in gear_ratio.values() if len(v) == 2)
    return result


@utils.timer
def main(data):

    part_1 = loop_through_chars(data)
    part_2 = loop_through_chars(data, part2=True)

    return part_1, part_2


if __name__ == "__main__":

    data = utils.get_data(3)
    part_1, part_2 = main(data)

    utils.print_solution(2023, 3, "Part 1", part_1)
    utils.print_solution(2023, 3, "Part 2", part_2)
