from collections import defaultdict
from itertools import combinations
from typing import Any

from utils import get_data, timer


def is_within_bounds(point: tuple[int, int], grid: list[list[Any]]):
    """Check if a point is within grid boundaries."""
    return 0 <= point[0] < len(grid) and 0 <= point[1] < len(grid[0])


def calculate_antinode(
    point_1: tuple[int, int],
    point_2: tuple[int, int],
    grid: list[list[Any]],
) -> tuple[tuple[int, int], tuple[int, int]]:

    left = min(point_1, point_2, key=lambda x: x[1])
    right = max(point_1, point_2, key=lambda x: x[1])

    h_move = left[1] - right[1]
    v_move = left[0] - right[0]

    antinode = [
        (left[0] + v_move, left[1] + h_move),
        (right[0] - v_move, right[1] - h_move),
    ]

    result = [anti for anti in antinode if is_within_bounds(anti, grid)]

    return result


def calculate_resonant_harmonic_antinode(
    point_1: tuple[int, int],
    point_2: tuple[int, int],
    grid: list[list[Any]],
) -> tuple[tuple[int, int], tuple[int, int]]:

    left = min(point_1, point_2, key=lambda x: x[1])
    right = max(point_1, point_2, key=lambda x: x[1])

    h_move = left[1] - right[1]
    v_move = left[0] - right[0]

    anti_1, anti_2 = left, right

    results = []

    while is_within_bounds(anti_1, grid) or is_within_bounds(anti_2, grid):

        if is_within_bounds(anti_1, grid):
            results.append(anti_1)

        if is_within_bounds(anti_2, grid):
            results.append(anti_2)

        anti_1 = (anti_1[0] + v_move, anti_1[1] + h_move)
        anti_2 = (anti_2[0] - v_move, anti_2[1] - h_move)

    return results


@timer
def main(data):

    antenna_hash = defaultdict(list)

    for i in range(len(data)):
        for j in range(len(data[0])):
            pos = data[i][j]
            if pos != "." and pos.isalnum():
                antenna_hash[pos].append((i, j))

    result_1 = []
    result_2 = []
    for symbol in antenna_hash.keys():
        for p1, p2 in combinations(antenna_hash[symbol], 2):
            anti_arr = calculate_antinode(p1, p2, data)
            resonant = calculate_resonant_harmonic_antinode(p1, p2, data)

            result_1.extend(anti_arr)
            result_2.extend(resonant)

    return len(set(result_1)), len(set(result_2))


if __name__ == "__main__":

    data = get_data(8)

    part_1, part_2 = main(data)
    print("Solution for Part 1", part_1)
    print("Solution for Part 2", part_2)
