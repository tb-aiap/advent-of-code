"""Solution for Day 13 2023."""

from typing import Iterator

import utils

ROW_VALUE = 100
COL_VALUE = 1


def get_blocks(data: list[str]) -> Iterator[list[str]]:
    result = []
    for line in data:
        if not line:
            yield result
            result = []
        else:
            result.append(line)

    if result:
        yield result


def find_smudge(block, l, r):
    return sum(a != b for a, b in zip(block[l], block[r]))


def solve(block: list[str], smudge=0) -> int:
    # start, end , steps, score
    for i in range(1, len(block)):
        l, r = i - 1, i
        smudge_count = 0

        while l >= 0 and r < len(block):
            smudge_diff = find_smudge(block, l, r)
            if block[l] == block[r] or smudge_diff == smudge:
                smudge_count += smudge_diff
                l -= 1
                r += 1
            else:
                break  # break skips else loop
        else:
            if smudge_count == smudge:
                return i
    return 0


@utils.timer
def main(data):
    part_1 = 0
    part_2 = 0
    for b in get_blocks(data):
        rotate_b = [r for r in zip(*b)]

        part_1 += solve(b) * ROW_VALUE
        part_1 += solve(rotate_b) * COL_VALUE

        part_2 += solve(b, smudge=1) * ROW_VALUE
        part_2 += solve(rotate_b, smudge=1) * COL_VALUE

    return part_1, part_2


if __name__ == "__main__":

    data = utils.get_data(13)
    part_1, part_2 = main(data)

    utils.print_solution(2023, 13, "Part 1", part_1)
    utils.print_solution(2023, 13, "Part 2", part_2)
