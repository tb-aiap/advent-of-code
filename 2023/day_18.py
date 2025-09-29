"""Solution for Day 18 2023."""

from typing import Iterator

import utils

Coord = tuple[int, int]

DIG = {
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1),
}


def parse_data(data) -> Iterator[tuple[str, str, str]]:
    for line in data:
        direction, length, colour = line.split(" ")
        yield direction, length, colour


def pick_and_shoelace(visited: list[tuple[int, int]], boundary: int):
    """using reddit's suggestion for the combination of 2 formula.

    To find the area of a polygon
    https://en.wikipedia.org/wiki/Shoelace_formula

    Using the area and pipe boundary to determine the interior boundary.
    https://en.wikipedia.org/wiki/Pick's_theorem
    """
    points_sum = 0
    for i in range(len(visited)):
        y0, x0 = visited[i - 1]
        y1, x1 = visited[i]

        points_sum += (x0 * y1) - (x1 * y0)

    area = abs(points_sum) / 2
    # pick formula
    # area = i + (b/2) - 1
    # i = area - (b/2) + l
    b = boundary
    i = area - (b / 2) + 1

    return i


def solve(data, part2: bool = False):
    arr: list[Coord] = []
    row, col = 0, 0
    boundary = 0
    for d, l, c in parse_data(data):
        if part2:
            # overwrite l and d
            l = int(c.strip("()")[1:-1], 16)
            # fmt: off
            match c.strip("()")[-1]:
                case "0": d = "R"
                case "1": d = "D"
                case "2": d = "L"
                case "3": d = "U"
            # fmt: on

        direction = DIG[d]
        row += direction[0] * int(l)
        col += direction[1] * int(l)
        boundary += int(l)
        arr.append((row, col))
    return boundary + pick_and_shoelace(arr, boundary)


@utils.timer
def main(data):

    part_1 = solve(data)
    part_2 = solve(data, part2=True)

    return part_1, part_2


if __name__ == "__main__":

    data = utils.get_data(18)
    part_1, part_2 = main(data)

    utils.print_solution(2023, 18, "Part 1", part_1)
    utils.print_solution(2023, 18, "Part 2", part_2)
