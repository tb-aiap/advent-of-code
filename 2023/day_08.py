"""Solution for Day 8 2023."""

import itertools
import math
import re
from typing import Iterator

import utils


def camel_direction(direction: str) -> Iterator[str]:
    """Loop through the directions endlessly."""
    for i in itertools.cycle(direction):
        yield i


def solve(direction: str, maps: list[str]):
    """Solution for part 1."""
    hashmap = {}
    camel_move = camel_direction(direction)
    for mapping in maps:
        k, l, r = re.findall("(\w+)", mapping)
        hashmap[k] = (l, r)

    pos = "AAA"
    steps = 0
    while pos != "ZZZ":
        d = next(camel_move)
        steps += 1
        if d == "L":
            pos = hashmap[pos][0]
        else:
            pos = hashmap[pos][1]

    return steps


def solve_2(direction: str, maps: list[str]):
    """Solution for"""
    hashmap = {}
    camel_move = camel_direction(direction)
    for mapping in maps:
        k, l, r = re.findall("(\w+)", mapping)
        hashmap[k] = (l, r)

    pos = [k for k in hashmap if k.endswith("A")]
    lcm = []
    for p in pos:
        steps = 0
        curr = p
        while not curr.endswith("Z"):
            d = next(camel_move)
            steps += 1
            if d == "L":
                curr = hashmap[curr][0]
            else:
                curr = hashmap[curr][1]
        lcm.append(steps)

    return lcm


@utils.timer
def main(data):

    part_1 = solve(data[0], data[2:])
    part_2 = math.lcm(*solve_2(data[0], data[2:]))

    return part_1, part_2


if __name__ == "__main__":

    data = utils.get_data(8)
    part_1, part_2 = main(data)

    utils.print_solution(2023, 8, "Part 1", part_1)
    utils.print_solution(2023, 8, "Part 2", part_2)
