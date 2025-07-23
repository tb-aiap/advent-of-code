"""Solution for Day 6 2023."""

import re
from functools import reduce
from operator import mul

import utils


def solve_1(distance: int, time: int):
    """Manually check each combination for the race."""
    ways_to_win = 0

    for s in range(1, time):
        remaining_time = time - s
        time_taken = distance / s
        if time_taken < remaining_time:
            ways_to_win += 1

    return ways_to_win


def binary_search(distance: int, time: int, from_end: bool = True):
    """Binary search to find minimum start time, and max end time that still wins race."""
    l = 1
    r = time - 1

    while l <= r:
        mid = (l + r) // 2  # mid is speed

        remaining_time = time - mid
        time_taken = distance / mid
        if time_taken < remaining_time:
            # can win with this speed,
            if from_end:
                l = mid + 1  # keep holding longer
            else:
                r = mid - 1  # the other way, keep holding shorter.
        else:
            # cannot win,
            if from_end:
                r = mid - 1
            else:
                l = mid + 1

    return r if from_end else l


@utils.timer
def main(data):
    time_str = re.findall("(\d+)", data[0])
    dist_str = re.findall("(\d+)", data[1])

    time_taken = list(map(int, time_str))
    distance = list(map(int, dist_str))
    part_1 = reduce(mul, (solve_1(d, t) for d, t in zip(distance, time_taken)))

    t = int("".join(time_str))
    d = int("".join(dist_str))
    part_2 = binary_search(d, t) - binary_search(d, t, False) + 1

    return part_1, part_2


if __name__ == "__main__":

    data = utils.get_data(6)
    part_1, part_2 = main(data)

    utils.print_solution(2023, 6, "Part 1", part_1)
    utils.print_solution(2023, 6, "Part 2", part_2)
