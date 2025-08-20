"""Solution for Day 14 2023."""

from collections import defaultdict
from typing import Iterable

import utils

ROCK = "O"
CUBE = "#"
EMPTY = "."
CYCLE = 1_000_000_000


def tilt_westwards(row: Iterable[str]) -> list[str]:
    """Using loops, so westward is the easiest to implement."""
    stack = []
    counter = defaultdict(int)
    for pos, rock in enumerate(row):
        if row[pos] == CUBE:
            if ROCK in counter:
                stack += [ROCK] * counter[ROCK]
            if EMPTY in counter:
                stack += [EMPTY] * counter[EMPTY]
            counter = defaultdict(int)
            stack += [CUBE]
        else:
            counter[rock] += 1

    if ROCK in counter:
        stack += [ROCK] * counter[ROCK]
    if EMPTY in counter:
        stack += [EMPTY] * counter[EMPTY]

    return stack


def anti_clockwise(data) -> list[tuple[str]]:
    return [d for d in zip(*data)][::-1]


def clockwise(data) -> list[tuple[str]]:
    return [d[::-1] for d in zip(*data)]


def tilt_north(data) -> list[tuple[str]]:
    rotate_data = anti_clockwise(data)
    titled_data = (tilt_westwards(r) for r in rotate_data)
    return clockwise(titled_data)


def tilt_south(data) -> list[tuple[str]]:
    rotate_data = clockwise(data)
    titled_data = [tilt_westwards(r) for r in rotate_data]
    return anti_clockwise(titled_data)


def tilt_east(data) -> list[tuple[str]]:
    rotate_data = [d[::-1] for d in data]
    titled_data = (tilt_westwards(r) for r in rotate_data)
    return [r[::-1] for r in titled_data]


def tilt_west(data) -> list[tuple[str]]:
    return [tilt_westwards(r) for r in data]


def one_cycle(data) -> list[tuple[str]]:
    return tilt_east(tilt_south(tilt_west(tilt_north(data))))


def measure_weight(data: Iterable[str]) -> int:
    total_weight = 0
    for i in range(len(data)):
        weight = len(data) - i
        total_weight += sum(1 * weight for w in data[i] if w == ROCK)

    return total_weight


def simulate_cycle(data) -> tuple[tuple[str]]:
    i = 0
    hashmap = {}
    cycle_board = data
    while True:
        cycle_board = tuple(tuple(i) for i in one_cycle(cycle_board))
        i += 1
        if cycle_board in hashmap:
            first_seen, second_seen = hashmap[cycle_board], i
            break
        else:
            hashmap[cycle_board] = i

    cycle = (CYCLE - first_seen) % (second_seen - first_seen) + first_seen

    cycle_board = data
    for _ in range(cycle):
        cycle_board = tuple(tuple(i) for i in one_cycle(cycle_board))

    return cycle_board


@utils.timer
def main(data):

    part_1 = measure_weight(tilt_north(data))
    part_2 = measure_weight(simulate_cycle(data))

    return part_1, part_2


if __name__ == "__main__":

    data = utils.get_data(14)
    part_1, part_2 = main(data)

    utils.print_solution(2023, 14, "Part 1", part_1)
    utils.print_solution(2023, 14, "Part 2", part_2)
