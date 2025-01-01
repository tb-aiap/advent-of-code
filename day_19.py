"""Solution for Day 19 2024."""

import utils


def dp_make_design(design: str, towels: list[str]):
    """
    DP to make design.
    if the first sequence uses "x" or "xx" or "xxx" etc,
    (i - len(t) + 1) is 0, where the towel extend all the way to the start.
    """
    dp = [0] * len(design)

    for i in range(len(design)):
        for t in towels:
            t_slice = slice(i - len(t) + 1, i + 1)

            if (i - len(t) + 1) == 0 and t == design[t_slice]:
                dp[i] += 1
            elif t == design[t_slice]:
                dp[i] += dp[i - len(t)]

    return dp[-1]


@utils.timer
def main(data: list[str]):

    towels = data[0].split(", ")
    designs = data[2:]

    dp_result = [dp_make_design(d, towels) for d in designs]

    part_1 = sum(map(bool, dp_result))
    part_2 = sum(dp_result)

    return part_1, part_2


if __name__ == "__main__":

    data = utils.get_data(19)
    part_1, part_2 = main(data)

    utils.print_solution(2024, 19, "Part 1", part_1)
    utils.print_solution(2024, 19, "Part 2", part_2)
