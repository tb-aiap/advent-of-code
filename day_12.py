"""Solution for 2024 day 12."""

from collections import defaultdict
from enum import Enum
from itertools import chain

from utils import get_data, is_within_bounds, timer


class Direction(Enum):
    # row, col
    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)


def search_dir(r, c, dir: Direction, grid):

    row_dir, col_dir = dir.value
    target_row, target_col = r + row_dir, c + col_dir

    if is_within_bounds((target_row, target_col), grid):
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


def get_sides(r, c, dir, grid) -> list[tuple[int, int]]:

    sides = []
    target = grid[r][c]
    for dir in Direction:
        row_dir, col_dir = dir.value
        target_row, target_col = r + row_dir, c + col_dir

        if (
            is_within_bounds((target_row, target_col), grid)
            and grid[target_row][target_col] != target
        ):
            sides.append((target_row, target_col))

        elif not is_within_bounds((target_row, target_col), grid):
            sides.append((row_dir, col_dir))

    return sides


def dfs(
    r: int,
    c: int,
    target: str,
    visited: set[tuple[int, int]],
    grid: list[list[str]],
):

    if not is_within_bounds((r, c), grid) or grid[r][c] != target or (r, c) in visited:
        return

    visited.add((r, c))

    dfs(r + 1, c, target, visited, grid)
    dfs(r - 1, c, target, visited, grid)
    dfs(r, c - 1, target, visited, grid)
    dfs(r, c + 1, target, visited, grid)

    return visited


@timer
def main(data):

    cost_hash = defaultdict(int)
    visited_hash = defaultdict(set)

    for r_idx, _ in enumerate(data):
        for c_idx, c in enumerate(data[r_idx]):
            if (r_idx, c_idx) in visited_hash[c]:
                continue
            visited = set()
            dfs(r_idx, c_idx, c, visited, data)
            visited_hash[c].update(visited)
            print((r_idx, c_idx), c, visited)
            perimeter = sum(
                get_perimeter(pos[0], pos[1], Direction, data) for pos in visited
            )
            print("SIDES for", c)
            print(
                set(
                    chain.from_iterable(
                        get_sides(pos[0], pos[1], Direction, data) for pos in visited
                    )
                )
            )

            cost_hash[c] += perimeter * len(visited)
            print()

    print(cost_hash)
    print(sum(i for i in cost_hash.values()))
    part_1 = sum(i for i in cost_hash.values())
    part_2 = 0

    return part_1, part_2


if __name__ == "__main__":

    data = get_data(12)

    part_1, part_2 = main(data)

    print("Solution for Part 1", part_1)
    print("Solution for Part 2", part_2)
