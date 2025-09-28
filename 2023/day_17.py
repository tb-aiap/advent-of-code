"""Solution for Day 17 2023."""

import heapq
from collections import defaultdict

import utils

DIR_REVERSE = {
    (1, 0): (-1, 0),
    (-1, 0): (1, 0),
    (0, 1): (0, -1),
    (0, -1): (0, 1),
}


def solve(data, min_step, max_step):
    start = (0, 0)
    target = (len(data) - 1, len(data[0]) - 1)

    # queue as total_distance, (row, col) , (dir_row, dir_col), steps
    queue = [(0, start, (1, 0), 0), (0, start, (0, 1), 0)]

    distance_hash = defaultdict(lambda: float("inf"))
    distance_hash[(start, (1, 0), 1)] = 0
    distance_hash[(start, (0, 1), 1)] = 0

    while queue:
        total_heat, pos, direction, steps = heapq.heappop(queue)

        if pos == target and steps > min_step:
            return total_heat

        # visited the neighbors
        for d in [e.value for e in utils.Direction]:
            nr, nc = pos[0] + d[0], pos[1] + d[1]

            if (
                not utils.is_within_bounds((nr, nc), data)
                or DIR_REVERSE[direction] == d
            ):
                continue

            if direction == d:
                new_step = steps + 1
                if new_step > max_step:
                    continue
            else:
                if steps < min_step:
                    continue
                new_step = 1

            heat = int(data[nr][nc])
            current_heat = total_heat + heat
            key = ((nr, nc), d, new_step)
            if current_heat < distance_hash[key]:
                distance_hash[key] = current_heat
                heapq.heappush(queue, (current_heat, (nr, nc), d, new_step))

    return -1


@utils.timer
def main(data):
    part_1 = solve(data, min_step=0, max_step=3)
    part_2 = solve(data, min_step=4, max_step=10)

    return part_1, part_2


if __name__ == "__main__":

    data = utils.get_data(17)
    part_1, part_2 = main(data)

    utils.print_solution(2023, 17, "Part 1", part_1)
    utils.print_solution(2023, 17, "Part 2", part_2)
