"""Solution for Day 12 2023."""

import re

import utils


def convert_records_to_num(records: str) -> list[int]:
    """Conditions ##.###.# to numbers 1,3,1"""
    r = re.findall("#+", records)
    return list(map(len, r))


def find_combination(conditions: str, condition_arr: list[int]):

    memo = {}

    def dp(c_idx: int, g_idx: int, dmg_count: int) -> int:
        """step through each character 1 by 1, and check for valid condition each step.

        Args:
            c_idx (int): idx of the condition
            g_idx (int): idx of condition array
            dmg_count (int): number of # gathered so far

        Returns:
            int: number of valid ways upon reaching the end.
        """
        key = (c_idx, g_idx, dmg_count)
        if key in memo:
            return memo[key]

        # base case
        if c_idx == len(conditions):
            if g_idx == len(condition_arr) and dmg_count == 0:
                return 1
            if g_idx == len(condition_arr) - 1 and dmg_count == condition_arr[g_idx]:
                return 1
            return 0

        char = conditions[c_idx]
        way = 0
        if char in ".?":
            if dmg_count == 0:
                way += dp(c_idx + 1, g_idx, dmg_count)
            elif dmg_count == condition_arr[g_idx] and g_idx < len(condition_arr):
                way += dp(c_idx + 1, g_idx + 1, 0)

        if char in "#?":
            if g_idx < len(condition_arr) and dmg_count < condition_arr[g_idx]:
                way += dp(c_idx + 1, g_idx, dmg_count + 1)

        memo[key] = way
        return way

    return dp(0, 0, 0)


@utils.timer
def main(data):

    part_1 = 0
    part_2 = 0
    for row in data:
        conditions, conditions_arr = row.split(" ")
        conditions_arr = list(map(int, conditions_arr.split(",")))

        part_1 += find_combination(conditions, conditions_arr)

        unfolded_conditions = "?".join([conditions] * 5)
        part_2 += find_combination(unfolded_conditions, conditions_arr * 5)

    return part_1, part_2


if __name__ == "__main__":

    data = utils.get_data(12)
    part_1, part_2 = main(data)

    utils.print_solution(2023, 12, "Part 1", part_1)
    utils.print_solution(2023, 12, "Part 2", part_2)
