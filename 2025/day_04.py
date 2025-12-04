"""Solution for Day 4 2025."""

import utils

ADJACENT = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
]


def count_surrounding(r, c, data):
    result = 0
    for d in ADJACENT:
        nr, nc = r + d[0], c + d[1]
        if 0 <= nr < len(data) and 0 <= nc < len(data[0]) and data[nr][nc] == "@":
            result += 1
    return result


def solve(data: list[str], part2: bool = False):
    result = 0
    while True:
        replaced = []
        for r in range(len(data)):
            for c in range(len(data[r])):
                if data[r][c] == "@" and count_surrounding(r, c, data) < 4:
                    result += 1
                    replaced.append((r, c))

        if not part2 or not replaced:
            break

        data_arr = [list(row) for row in data]
        for coor in replaced:
            data_arr[coor[0]][coor[1]] = "."

        data = ["".join(row) for row in data_arr]

    return result


@utils.timer
def main(data):
    part_1 = solve(data)
    part_2 = solve(data, part2=True)

    return part_1, part_2


if __name__ == "__main__":

    data = utils.get_data(4)
    part_1, part_2 = main(data)

    utils.print_solution(2025, 4, "Part 1", part_1)
    utils.print_solution(2025, 4, "Part 2", part_2)
