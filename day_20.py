"""Solution for Day 20 2024."""

from collections import defaultdict, deque
from itertools import chain

import utils


def get_pos(position: str, grid: list[list[str]]) -> tuple[int, int]:
    "Get coordiante for the specific string, S or E"
    for ridx, r in enumerate(grid):
        if position in r:
            cidx = grid[ridx].index(position)
            return ridx, cidx


def cheat_here(position: tuple[int, int], grid: list[list[str]]):

    cheat_arr = set()
    for dir in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        block_row = position[0] + dir[0]
        block_col = position[1] + dir[1]

        cheat_row = block_row + dir[0]
        cheat_col = block_col + dir[1]

        if (
            utils.is_within_bounds((cheat_row, cheat_col), grid)
            and grid[block_row][block_col] == "#"
            and grid[cheat_row][cheat_col] != "#"
        ):
            cheat_arr.add(((position), (cheat_row, cheat_col)))

    return cheat_arr


def scan_cheat(
    start: tuple[int, int],
    end: tuple[int, int],
):
    """Take shortest path horizontal and vertical within timelimit."""

    r = end[0] - start[0]
    c = end[1] - start[1]

    return abs(r) + abs(c)


def get_track(
    start: tuple[int, int],
    end: tuple[int, int],
    grid: list[list[str]],
    obstacle: list[str],
):

    visited = set()
    queue = deque()
    queue.append((start[0], start[1], [start]))

    while queue:
        row, col, path = queue.popleft()

        if (row, col) == end:
            return path

        for dir in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr = row + dir[0]
            nc = col + dir[1]
            new_path = path.copy()

            if (
                utils.is_within_bounds((nr, nc), grid)
                and (nr, nc) not in visited
                and grid[nr][nc] not in obstacle
            ):
                visited.add((nr, nc))
                new_path.append((nr, nc))
                queue.append((nr, nc, new_path))


@utils.timer
def main(grid: list[list[str]]):

    TIME_SAVE = 100
    start_pos = get_pos("S", grid)
    end_pos = get_pos("E", grid)
    cheat_hash = dict()
    shortest = get_track(start_pos, end_pos, grid, obstacle=["#"])
    result = 0
    for cheat_start, cheat_end in chain.from_iterable(
        cheat_here(coord, grid) for coord in shortest
    ):
        if shortest.index(cheat_end) > shortest.index(cheat_start):
            time_use = shortest.index(cheat_end) - shortest.index(cheat_start) - 2
            cheat_hash.setdefault(time_use, 0)
            cheat_hash[time_use] += 1
            if time_use >= 100:
                result += 1

    cheat_hash_2 = defaultdict(int)
    for idx, coord in enumerate(shortest):
        save_time = idx + TIME_SAVE
        for nidx in range(save_time, len(shortest)):
            cheat_path = scan_cheat(coord, shortest[nidx])
            time_saved = nidx - idx - cheat_path
            if cheat_path <= 20 and time_saved >= TIME_SAVE:
                cheat_hash_2[time_saved] += 1

    part_1 = result
    part_2 = sum(cheat_hash_2.values())

    return part_1, part_2


if __name__ == "__main__":

    data = utils.get_data(20)
    part_1, part_2 = main(data)

    utils.print_solution(2024, 20, "Part 1", part_1)
    utils.print_solution(2024, 20, "Part 2", part_2)
