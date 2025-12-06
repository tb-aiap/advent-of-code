"""Solution for Day 6 2025."""

from collections import defaultdict
from functools import reduce
from operator import add, mul

import utils

SIGN_OPERATOR = {
    "*": mul,
    "+": add,
}


def solve(data):
    qns_bank = defaultdict(list)
    signs = [s for s in data[-1].split(" ") if s]
    for row in data[:-1]:
        row_arr = [int(r) for r in row.split(" ") if r]
        for i, num in enumerate(row_arr):
            qns_bank[i].append(num)

    assert len(signs) == len(qns_bank)

    return sum(reduce(SIGN_OPERATOR[sign], qns_bank[i]) for i, sign in enumerate(signs))


def solve2(data):

    signs = [s for s in data[-1].split(" ") if s]

    single_sum = []
    problem_idx = 0
    result = 0
    for row in zip(*data[:-1]):
        # read the rows vertically
        row_val = "".join(row).strip()
        # print(row, problem_idx, len(signs))
        # print(signs)
        if row_val:
            single_sum.append(int(row_val))
        else:
            result += reduce(SIGN_OPERATOR[signs[problem_idx]], single_sum)
            problem_idx += 1
            single_sum = []

    # resolve remaining single sum
    if single_sum:
        result += reduce(SIGN_OPERATOR[signs[problem_idx]], single_sum)

    return result


@utils.timer
def main(data: list[str]):
    # pad and align starting text, util has stripped all spacing >.<
    first_col_max = max(len(row[: row.index(" ")]) for row in data)
    new_data = []

    for row in data[:-1]:
        if len(row[: row.index(" ")]) < first_col_max:
            pad = first_col_max - len(row[: row.index(" ")])
            new_data.append(" " * pad + row)
        else:
            new_data.append(row)
    max_row_len = max(len(row) for row in new_data)
    data = [r.ljust(max_row_len) for r in new_data + [data[-1]]]
    # adjustment to revert to raw data

    part_1 = solve(data)
    part_2 = solve2(data)

    return part_1, part_2
