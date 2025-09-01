"""Solution for Day 16 2023."""

import utils

HEADING = {
    "UP": (-1, 0),
    "DOWN": (1, 0),
    "LEFT": (0, -1),
    "RIGHT": (0, 1),
}


def through_split(r, c, d, tile) -> list[tuple[tuple[int, int]]]:
    """Running through - or |"""
    if tile == "-" and d in [HEADING["UP"], HEADING["DOWN"]]:
        return [((r, c), HEADING["LEFT"]), ((r, c), HEADING["RIGHT"])]

    if tile == "|" and d in [HEADING["LEFT"], HEADING["RIGHT"]]:
        return [((r, c), HEADING["UP"]), ((r, c), HEADING["DOWN"])]

    # else is a passthrough
    return [((r, c), d)]


def angle_mirror(r, c, d, tile) -> list[tuple[tuple[int, int]]]:
    """Running through \ or /"""
    angle_mapping = {
        "\\": {
            HEADING["DOWN"]: HEADING["RIGHT"],
            HEADING["UP"]: HEADING["LEFT"],
            HEADING["RIGHT"]: HEADING["DOWN"],
            HEADING["LEFT"]: HEADING["UP"],
        },
        "/": {
            HEADING["DOWN"]: HEADING["LEFT"],
            HEADING["UP"]: HEADING["RIGHT"],
            HEADING["RIGHT"]: HEADING["UP"],
            HEADING["LEFT"]: HEADING["DOWN"],
        },
    }
    return [((r, c), angle_mapping[tile][d])]


def pew_pew(start: tuple[int, int], start_dir: tuple[int, int], grid: list[list[str]]):
    """Send a light beam from outside the board into the board with certain direction.

    If sending into (0,0) towards right.
    start = (0, -1)
    start_dir = (0, 1)
    So that the next beam commence on (0, 0)
    """
    energized = set()
    stack = [(start, start_dir)]
    visited = set()

    while stack:
        (r, c), d = stack.pop()
        nr, nc = r + d[0], c + d[1]

        if not (0 <= nr and nr < len(grid) and 0 <= nc and nc < len(grid[0])):
            continue

        if (nr, nc, d) in visited:
            continue

        energized.add((nr, nc))
        visited.add((nr, nc, d))
        tile = grid[nr][nc]
        if tile == ".":
            stack.append(((nr, nc), d))
        elif tile in "-|":
            next_beam = through_split(nr, nc, d, tile)
            stack.extend(next_beam)
        elif tile in "\\/":
            next_beam = angle_mirror(nr, nc, d, tile)
            stack.extend(next_beam)

    # print(empty_board)
    return energized


def max_pew(grid: list[list[str]]):
    """Pew from various directions."""
    # top - down
    # left - right
    # bottom - up
    # right - left

    result = 0

    for c in range(len(grid[0])):
        energized = pew_pew((-1, c), HEADING["DOWN"], grid)
        result = max(result, len(energized))

        energized = pew_pew((len(grid), c), HEADING["UP"], grid)
        result = max(result, len(energized))

    for r in range(len(grid)):
        energized = pew_pew((r, -1), HEADING["RIGHT"], grid)
        result = max(result, len(energized))

        energized = pew_pew((r, len(grid[0])), HEADING["LEFT"], grid)
        result = max(result, len(energized))

    return result


@utils.timer
def main(data):

    START = (0, -1)
    START_DIR = HEADING["RIGHT"]

    b = pew_pew(START, START_DIR, data)

    part_1 = len(b)
    part_2 = max_pew(data)

    return part_1, part_2


if __name__ == "__main__":

    data = utils.get_data(16)
    part_1, part_2 = main(data)

    utils.print_solution(2023, 16, "Part 1", part_1)
    utils.print_solution(2023, 16, "Part 2", part_2)
