"""Solution for Day 5 2025."""

import utils


def solve(data):

    # initial data is a list of all lines. so rejoining to split by section
    fresh_range_str, ingredient_str = "\n".join(data).split("\n\n")

    fresh_count = set()
    for fr in fresh_range_str.splitlines():
        l, h = map(int, fr.split("-"))
        for ingredient in ingredient_str.splitlines():
            if l <= int(ingredient) <= h:
                fresh_count.add(ingredient)
    return len(fresh_count)


def solve2(data):
    # initial data is a list of all lines. so rejoining to split by section
    fresh_range_str, _ = "\n".join(data).split("\n\n")
    fresh_range = fresh_range_str.split("\n")
    fresh_range_arr = [tuple(map(int, fr.split("-"))) for fr in fresh_range]

    sorted_fresh_arr = sorted(fresh_range_arr, key=lambda x: x[0])

    merged_fresh_range = []

    # e.g 1 - 6
    for fr in sorted_fresh_arr:
        if not merged_fresh_range or merged_fresh_range[-1][1] < fr[0]:
            # 7 - 8
            merged_fresh_range.append(fr)
        elif merged_fresh_range[-1][1] >= fr[0]:
            l, h = merged_fresh_range.pop()
            merged_fresh_range.append((l, max(fr[1], h)))

    return sum(fr[1] - fr[0] + 1 for fr in merged_fresh_range)


@utils.timer
def main(data):

    part_1 = solve(data)
    part_2 = solve2(data)

    return part_1, part_2


if __name__ == "__main__":

    data = utils.get_data(5)
    part_1, part_2 = main(data)

    utils.print_solution(2025, 5, "Part 1", part_1)
    utils.print_solution(2025, 5, "Part 2", part_2)
