"""Solution for Day 16 2024."""

import heapq
import math
from collections import defaultdict
from dataclasses import dataclass

from utils import get_data, timer


@dataclass
class Point:
    """Helper class method to preprocess matric point (row/col)."""

    r: int
    c: int

    def to_tuple(self):
        return (self.r, self.c)

    def __add__(self, others):

        if isinstance(others, tuple):
            return Point(self.r + others[0], self.c + others[1])

        if isinstance(others, Point):
            return Point(self.r + others.r, self.c + others.c)


def get_pos(position: str, grid: list[list[str]]) -> tuple[int, int]:
    "Get coordiante for the specific string, S or E"
    for ridx, r in enumerate(grid):
        if position in r:
            cidx = grid[ridx].index(position)
            return ridx, cidx


def generate_distance_hash(grid):

    hash_arr = defaultdict(tuple)

    for ridx, _ in enumerate(grid):
        for cidx, v in enumerate(grid[ridx]):
            if v != ".":
                hash_arr[(ridx, cidx)] = (math.inf, None)

    return hash_arr


# DIR       left     up       right   down
DIRECTION = [(0, -1), (-1, 0), (0, 1), (1, 0)]


@timer
def main(data):

    end_pos = get_pos("E", data)
    start_pos = get_pos("S", data)
    start_dir = 2

    starting_src = (0, start_dir, *start_pos, [])
    queue = [starting_src]
    min_length = math.inf
    min_cost = dict()
    seats = set()

    while queue:
        score, direction, row, col, path = heapq.heappop(queue)
        if (row, col) == end_pos:
            min_length = min(min_length, score)
            if min_length >= score:
                curr_seats = {(x[1], x[2]) for x in new_path}
                seats.update(curr_seats)
            else:
                break

        if (direction, row, col) in min_cost and min_cost[
            (direction, row, col)
        ] < score:
            continue
        else:
            min_cost[(direction, row, col)] = score

        nr = row + DIRECTION[direction][0]
        nc = col + DIRECTION[direction][1]

        if data[nr][nc] in [".", "E"] and (direction, nr, nc) not in path:
            # go straight next
            new_path = path.copy()
            new_path.append((direction, nr, nc))
            heapq.heappush(queue, (score + 1, direction, nr, nc, new_path))

        left = (direction - 1) % 4
        right = (direction + 1) % 4

        if (left, row, col) not in path:
            new_path = path.copy()
            new_path.append((left, row, col))
            heapq.heappush(queue, (score + 1000, left, row, col, new_path))

        if (right, nr, col) not in path:
            new_path = path.copy()
            new_path.append((right, row, col))
            heapq.heappush(queue, (score + 1000, right, row, col, new_path))

    part_1, part_2 = min_length, len(seats)
    return part_1, part_2


if __name__ == "__main__":

    DAY = __file__.rsplit("_", maxsplit=1)[-1].rstrip(".py")
    data = get_data(DAY)
    part_1, part_2 = main(data)

    print("Solution for Part 1", part_1)
    print("Solution for Part 2", part_2)
