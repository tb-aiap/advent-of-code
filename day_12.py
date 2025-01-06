"""Solution for 2024 day 12."""

from collections import defaultdict
from enum import Enum
from itertools import chain

import utils


class Direction(Enum):
    # row, col
    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)


def search_dir(r, c, dir: Direction, grid):

    row_dir, col_dir = dir.value
    target_row, target_col = r + row_dir, c + col_dir

    if utils.is_within_bounds((target_row, target_col), grid):
        return grid[target_row][target_col]

    return "OB"


def get_perimeter(r, c, dir, grid):

    target = grid[r][c]
    perimeter = 0
    for dir in Direction:
        neighbor = search_dir(r, c, dir, grid)
        if neighbor == "OB" or neighbor != target:
            perimeter += 1

    return perimeter


def get_one_side(r, c, dir, grid) -> list[tuple[int, int]]:

    sides = []
    target = grid[r][c]

    row_dir, col_dir = dir.value
    target_row, target_col = r + row_dir, c + col_dir

    if (
        utils.is_within_bounds((target_row, target_col), grid)
        and grid[target_row][target_col] != target
    ):
        sides.append((target_row, target_col))

    elif not utils.is_within_bounds((target_row, target_col), grid):
        sides.append((target_row, target_col))

    return sides


def calculate_sides(dir_sides, direction):
    sides_hash = defaultdict(list)

    for i in sorted(dir_sides):
        if direction.name in ["UP", "DOWN"]:
            sides_hash[i[0]].append(i)
        if direction.name in ["LEFT", "RIGHT"]:
            sides_hash[i[1]].append(i)

    sides = 0
    for s in sides_hash:
        sides += 1
        if len(sides_hash[s]) > 1:
            for sw in utils.sliding_window(sides_hash[s], 2):
                if abs(sw[0][0] - sw[1][0]) > 1 or abs(sw[0][1] - sw[1][1]) > 1:
                    sides += 1
    return sides


def dfs(
    r: int,
    c: int,
    target: str,
    visited: set[tuple[int, int]],
    grid: list[list[str]],
):

    if (
        not utils.is_within_bounds((r, c), grid)
        or grid[r][c] != target
        or (r, c) in visited
    ):
        return

    visited.add((r, c))

    dfs(r + 1, c, target, visited, grid)
    dfs(r - 1, c, target, visited, grid)
    dfs(r, c - 1, target, visited, grid)
    dfs(r, c + 1, target, visited, grid)

    return visited


@utils.timer
def main(data):

    cost_hash = defaultdict(int)
    cost_side_hash = defaultdict(int)
    visited_hash = defaultdict(set)

    for r_idx, _ in enumerate(data):
        for c_idx, c in enumerate(data[r_idx]):
            if (r_idx, c_idx) in visited_hash[c]:
                continue
            ### For part 1
            # dfs on each new farm, and seach all the adjacent Letter
            visited = set()
            dfs(r_idx, c_idx, c, visited, data)
            visited_hash[c].update(visited)

            sides_part_2 = 0
            perimeter = sum(
                get_perimeter(pos[0], pos[1], Direction, data) for pos in visited
            )
            cost_hash[c] += perimeter * len(visited)

            ### For part 2
            # get the sides for each farm as an array
            # for each side, from up-down-left-right. hash the column/row respectively
            # for each side, if 2 points are not next to each other, its a different side.
            for dir in Direction:
                dir_sides = chain.from_iterable(
                    get_one_side(pos[0], pos[1], dir, data) for pos in visited
                )

                sides_part_2 += calculate_sides(dir_sides, dir)
            cost_side_hash[c] += sides_part_2 * len(visited)

    part_1 = sum(i for i in cost_hash.values())
    part_2 = sum(i for i in cost_side_hash.values())

    return part_1, part_2


if __name__ == "__main__":

    data = utils.get_data(12)
    part_1, part_2 = main(data)

    utils.print_solution(2024, 12, "Part 1", part_1)
    utils.print_solution(2024, 12, "Part 2", part_2)
