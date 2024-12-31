"""Solution for Day 18 2024."""

from collections import deque

import utils


def get_coords(data: list[str]):
    for s in data:
        yield map(int, s.split(","))


def bfs(start: tuple[int, int], end: tuple[int, int], grid: list[list[str]]):
    """Using BFS to get the shortest path, including tracked path.

    Args:
        start (tuple[int, int]): Starting position
        end (tuple[int, int]): Ending position
        grid (list[list[str]]): The maze
    """
    path = [(start)]
    visited = set()
    queue = deque()
    queue.append((*start, path))

    while queue:
        r, c, curr_path = queue.popleft()

        if (r, c) == end:
            print("Path include (0,0)", len(curr_path), curr_path)
            return len(curr_path)

        for dir in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nr, nc = r + dir[0], c + dir[1]
            if (
                (nr, nc) not in visited
                and utils.is_within_bounds((nr, nc), grid)
                and grid[nr][nc] == "."
            ):
                visited.add((nr, nc))
                new_path = curr_path.copy()
                new_path.append((nr, nc))
                queue.append((nr, nc, new_path))


@utils.timer
def main(data):

    coords = get_coords(data)

    if len(data) < 1024:
        size, b, end = 7, 12, (6, 6)
    else:
        size, b, end = 71, 1024, (70, 70)

    grid = [["."] * size for _ in range(size)]

    for _ in range(b):
        x, y = next(coords)
        grid[y][x] = "#"

    part_1 = bfs((0, 0), end, grid) - 1

    # simulate remaining bytes falling get_coords iterator.
    while True:
        x, y = next(coords)
        grid[y][x] = "#"
        if bfs((0, 0), end, grid) is None:
            # if no path after exhausting all queue
            break

    part_2 = f"{x},{y}"

    return part_1, part_2


if __name__ == "__main__":

    DAY = __file__.rsplit("_", maxsplit=1)[-1].rstrip(".py")
    data = utils.get_data(DAY)
    part_1, part_2 = main(data)

    utils.print_solution(2024, DAY, "Part 1", part_1)
    utils.print_solution(2024, DAY, "Part 2", part_2)
