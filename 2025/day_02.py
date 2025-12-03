"""Solution for Day 2 2025."""

import math

import utils


def count_digit(n: int) -> int:
    """Trying math log10 to count digit."""
    return 1 if n == 0 else int(math.log10(n)) + 1


def find_invalid_ids_str(start, high, result, part2=False) -> None:
    """Convert int to str to count digit and back to int.

    Example:
            12 repeated -> 1212
            5 repeated  -> 5555
    """
    half_len = count_digit(start) // 2
    start_str = str(start)
    split_start = 1 if part2 else half_len

    for i in range(split_start, half_len + 1):
        digit_pair = start_str[:i]
        multiply_by = len(start_str) // i

        if len(digit_pair) * multiply_by == len(start_str):
            # construct starting combi eg 123 to max possible 999s
            max_range = int("9" * len(digit_pair))
            for j in range(int(digit_pair), max_range + 1):
                invalid_pair = int(str(j) * multiply_by)
                if start <= invalid_pair <= high:
                    result.append(invalid_pair)
    return


def solve(data, part2=False):

    result: list[int] = []
    data_arr: list[str] = data[0].split(",")
    for interval in data_arr:
        low, high = interval.split("-")
        start, high = int(low), int(high)
        while start <= high:
            num_of_digit = count_digit(start)
            if num_of_digit % 2 == 0 or part2:
                find_invalid_ids_str(start, high, result, part2)

            start = 10 ** (num_of_digit)

    return sum(set(result))


@utils.timer
def main(data):

    part_1 = solve(data)
    part_2 = solve(data, part2=True)

    return part_1, part_2


if __name__ == "__main__":

    data = utils.get_data(2)
    part_1, part_2 = main(data)

    utils.print_solution(2025, 2, "Part 1", part_1)
    utils.print_solution(2025, 2, "Part 2", part_2)
