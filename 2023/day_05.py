"""Solution for Day 5 2023."""

import re
from collections import defaultdict
from typing import Any, Iterator

import utils


def get_seed_array(seed_str: str) -> list[int]:
    """Parse the seed line into seed array."""
    result = re.findall("(\d+)", seed_str)
    return [int(i) for i in result]


def get_seed_array_range(seed_str: str) -> Iterator[tuple[int]]:
    """Parse the seed array into intervals."""
    arr = get_seed_array(seed_str)
    for i in range(0, len(arr), 2):
        yield (arr[i], arr[i] + arr[i + 1] - 1)


def create_almanac_hash(data: list[Any]):
    """Parse the mappings into dictionary of intervals."""
    i = 0
    result = defaultdict(list)
    mapping = 0
    while i < len(data):
        if not "map" in data[i]:
            i += 1
            continue
        mapping += 1
        while i < len(data) - 1 and len(data[i + 1]) > 1:
            nums = list(map(int, data[i + 1].split(" ")))

            result[mapping].append(
                ((nums[1], nums[1] + nums[2] - 1), (nums[0], nums[0] + nums[2] - 1))
            )
            i += 1
    return result


def map_range_to_range(
    seed_range: tuple[int, int],
    mapping: tuple[tuple[int]],
) -> tuple[tuple[int, int], tuple[int, int]]:
    """from src range, output a tuple of target range."""
    src_s, src_e = seed_range
    overlapped_result = []
    unmapped_result = []
    src, dest = mapping
    interval = dest[0] - src[0]
    if interval != dest[1] - src[1]:
        raise Exception("expect both src and destination intervals to be similar.")

    overlap_start = max(src_s, src[0])
    overlap_end = min(src_e, src[1])

    if overlap_end < overlap_start:
        # no overlap.
        unmapped_result.append((src_s, src_e))
        return overlapped_result, unmapped_result

    # mapping partial no overlap area
    if src_s < src[0]:
        unmapped_result.append((src_s, src[0] - 1))

    if src_e > src[1]:
        unmapped_result.append((src[1] + 1, src_e))

    # confirmed overlapped areas
    overlapped_result.append((overlap_start + interval, overlap_end + interval))

    return overlapped_result, unmapped_result


def solve_1(seed: int, alamach_hash: dict[int, tuple[tuple[int]]]) -> int:
    """Solution for part 1."""
    left = seed
    for i in range(1, len(alamach_hash) + 1):
        assigned = False
        for src, dest in alamach_hash[i]:
            if src[0] <= left <= src[1]:
                diff = left - src[0]
                left = dest[0] + diff
                assigned = True
                break
        if not assigned:
            left = left
        assigned = False

    return left


def solve_2(seed_str: str, alamach_hash: dict[tuple[tuple[int]]]) -> list[tuple[int]]:

    seed_arr = get_seed_array_range(seed_str)
    left_interval = [(i, 1) for i in seed_arr]
    result = []
    while left_interval:
        left, level = left_interval.pop()

        if level == 8:
            result.append(left)
            continue

        unmapped = [left]
        for mapping in alamach_hash[level]:
            temp_overlap = []
            for unmap in unmapped:
                overlapped, no_overlap = map_range_to_range(unmap, mapping)

                if overlapped:
                    left_interval.extend([(r, level + 1) for r in overlapped])
                temp_overlap.extend(no_overlap)
            unmapped = temp_overlap
        left_interval.extend([(r, level + 1) for r in unmapped])
    return result


@utils.timer
def main(data):
    almamac_hash = create_almanac_hash(data)

    part_1 = min(solve_1(s, almamac_hash) for s in get_seed_array(data[0]))
    part_2 = min(i[0] for i in solve_2(data[0], almamac_hash))

    return part_1, part_2


if __name__ == "__main__":

    data = utils.get_data(5)
    part_1, part_2 = main(data)

    utils.print_solution(2023, 5, "Part 1", part_1)
    utils.print_solution(2023, 5, "Part 2", part_2)
