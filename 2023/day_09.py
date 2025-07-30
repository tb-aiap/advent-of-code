"""Solution for Day 9 2023."""

import re

import utils


def get_next_value(arr: list[int]):
    result = [arr[i] - arr[i - 1] for i in range(1, len(arr))]
    return result


def solve(arr: list[int], part2: bool = False):
    diff_arr = arr
    result = 0
    result_2 = []
    while diff_arr[-1] != 0 and len(set(diff_arr)) >= 1:
        if part2:
            result_2.append(diff_arr[0])
        result += diff_arr[-1]
        diff_arr = get_next_value(diff_arr)
    # counting up from top, we get c using a - b = c
    # 5  10  13  16  21  30  45
    #   5   3   3   5   9  15
    #    -2   0   2   4   6
    #       2   2   2   2
    #         0   0   0
    # 5  10  13  16  21  30  45
    #   5   3   3   5   9  15
    #    -2   0   2   4   6
    #       b   a   2   2
    #         c   0   0
    # a - b = c
    # b = a - c
    if part2:
        b = None
        c = 0
        for i in reversed(result_2):
            a = i
            b = a - c
            c = b
        return b
    return result


@utils.timer
def main(data):
    data_arr = [list(map(int, re.findall("([-]?\d+)", d))) for d in data]
    part_1 = sum(solve(d) for d in data_arr)

    # data_arr = [list(map(int, re.findall("([-]?\d+)", d))) for d in data]
    part_2 = sum(solve(d, part2=True) for d in data_arr)

    return part_1, part_2


if __name__ == "__main__":

    data = utils.get_data(9)
    part_1, part_2 = main(data)

    utils.print_solution(2023, 9, "Part 1", part_1)
    utils.print_solution(2023, 9, "Part 2", part_2)
