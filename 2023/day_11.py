"""Solution for Day 11 2023."""

from itertools import combinations
from typing import TypeAlias

import utils

Coords: TypeAlias = tuple[int, int]

GALAXY = "#"


def get_galaxy_index(grid: list[list[str]]) -> list[Coords]:
    """Returns index of all galaxies."""
    result = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == GALAXY:
                result.append((i, j))
    return result


def get_empty_rows(grid: list[list[str]], column: bool = False) -> list[Coords]:
    """Identify rows without Galaxy."""
    if column:
        grid = [g for g in zip(*grid)]
    return [i for i, line in enumerate(grid) if GALAXY not in line]


def solve(data, expansion_rate=2):
    """Solve for Day 11."""
    galaxy = get_galaxy_index(data)
    empty_row_data = get_empty_rows(data)
    empty_col_data = get_empty_rows(data, column=True)
    g_pair = combinations(galaxy, r=2)

    empty_row = [1 if i in empty_row_data else 0 for i in range(len(data))]
    empty_col = [1 if i in empty_col_data else 0 for i in range(len(data[0]))]

    result = 0
    for p1, p2 in g_pair:
        path = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        e = 0  # expansion
        e_add = expansion_rate - 1

        small_r = min(p1[0], p2[0])
        big_r = max(p1[0], p2[0])
        e += sum(empty_row[small_r : big_r + 1]) * e_add

        small_c = min(p1[1], p2[1])
        big_c = max(p1[1], p2[1])
        e += sum(empty_col[small_c : big_c + 1]) * e_add

        temp = path + e
        result += temp

    return result


@utils.timer
def main(data: list[list[str]]):

    part_1 = solve(data)
    part_2 = solve(data, expansion_rate=1_000_000)

    return part_1, part_2


if __name__ == "__main__":

    data = utils.get_data(11)
    part_1, part_2 = main(data)

    utils.print_solution(2023, 11, "Part 1", part_1)
    utils.print_solution(2023, 11, "Part 2", part_2)
