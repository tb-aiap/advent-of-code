"""Solution for Day 9 2025."""

import utils


def solve(data):
    coords = [list(map(int, c.split(","))) for c in data]
    result = 0
    for x1, y1 in coords:
        for x2, y2 in coords:
            x_area = abs(x1 - x2) + 1
            y_area = abs(y1 - y2) + 1
            result = max(result, x_area * y_area)

    return result


def solve2(data): ...


@utils.timer
def main(data):

    part_1 = solve(data)
    part_2 = None

    return part_1, part_2


if __name__ == "__main__":

    data = utils.get_data(9)
    part_1, part_2 = main(data)

    utils.print_solution(2025, 9, "Part 1", part_1)
    utils.print_solution(2025, 9, "Part 2", part_2)
