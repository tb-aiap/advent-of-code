from collections import defaultdict
from itertools import combinations
from typing import Any

from utils import get_data, timer


def calculate_antinode(
    point_1: tuple[int, int],
    point_2: tuple[int, int],
) -> tuple[tuple[int, int], tuple[int, int]]:

    left = min(point_1, point_2, key=lambda x: x[1])
    right = max(point_1, point_2, key=lambda x: x[1])

    h_move = left[1] - right[1]
    v_move = left[0] - right[0]

    antinode_1 = (left[0] + v_move, left[1] + h_move)
    antinode_2 = (right[0] - v_move, right[1] - h_move)

    return antinode_1, antinode_2


def point_within_bound(point: tuple[int, int], grid: list[list[Any]]):

    return (
        point[0] >= 0
        and point[0] < len(grid)
        and point[1] >= 0
        and point[1] < len(grid[0])
    )


@timer
def main(data):

    antenna_hash = defaultdict(list)

    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] != "." and data[i][j].isalnum():
                antenna_hash[data[i][j]].append((i, j))
    # print(antenna_hash)

    result = []
    for symbol in antenna_hash.keys():
        for p1, p2 in combinations(antenna_hash[symbol], 2):

            antinode_1, antinode_2 = calculate_antinode(p1, p2)

            for anti in [antinode_1, antinode_2]:
                if point_within_bound(anti, data):
                    result.append(anti)

    return len(set(result))


if __name__ == "__main__":

    data = get_data(8)
    print(data)

    part_1 = main(data)
    print("Solution for Part 1", part_1)
