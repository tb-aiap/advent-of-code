"""Solution for Day 20 2024."""

from collections import deque

import utils


def get_pos(position: str, grid: list[list[str]]) -> tuple[int, int]:
    "Get coordiante for the specific string, S or E"
    for ridx, r in enumerate(grid):
        if position in r:
            cidx = grid[ridx].index(position)
            return ridx, cidx


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
    """BFS to get shortest path track."""
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


def cheat(shortest_path, time_save, cheat_limit):
    """Try to cheat by skipping X seconds ahead, with available cheat limit."""
    ans = 0
    for idx, coord in enumerate(shortest_path):
        for nidx in range(idx + time_save, len(shortest_path)):
            cheat_path = scan_cheat(coord, shortest_path[nidx])
            time_saved = nidx - idx - cheat_path
            if cheat_path <= cheat_limit and time_saved >= time_save:
                ans += 1
    return ans


@utils.timer
def main(grid: list[list[str]]):

    start_pos = get_pos("S", grid)
    end_pos = get_pos("E", grid)
    shortest = get_track(start_pos, end_pos, grid, obstacle=["#"])

    print("Calculating answer.")
    part_1 = cheat(shortest, time_save=100, cheat_limit=2)
    part_2 = cheat(shortest, time_save=100, cheat_limit=20)

    return part_1, part_2


if __name__ == "__main__":

    data = utils.get_data(20)
    part_1, part_2 = main(data)

    utils.print_solution(2024, 20, "Part 1", part_1)
    utils.print_solution(2024, 20, "Part 2", part_2)
