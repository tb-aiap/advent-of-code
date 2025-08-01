"""Solution for Day 10 2023."""

import utils

DIR = ["UP", "RIGHT", "DOWN", "LEFT"]

DIR_REV = {
    "UP": "DOWN",
    "DOWN": "UP",
    "LEFT": "RIGHT",
    "RIGHT": "LEFT",
}

DIR_HASH = {
    "UP": (-1, 0),  # up
    "RIGHT": (0, 1),  # right
    "DOWN": (1, 0),  # down
    "LEFT": (0, -1),  # left
}

CURR_PIPES = {
    # (curr pipe), (out direction)
    "|": ("UP", "DOWN"),
    "-": ("LEFT", "RIGHT"),
    "L": ("UP", "RIGHT"),
    "J": ("UP", "LEFT"),
    "7": ("LEFT", "DOWN"),
    "F": ("RIGHT", "DOWN"),
}


def get_start_pos(arr: list[list[str]]) -> tuple[int, int]:
    """Look for char S, the starting position."""
    for r in range(len(arr)):
        if "S" in arr[r]:
            col = arr[r].index("S")
            starting_pos = (r, col)
            return starting_pos


def start_pipe_shape(starting_pos: tuple[int, int], arr: list[list[str, str]]):
    """Determine the shape of starting pipe S."""
    pipe_dir = []
    r, c = starting_pos
    for d, rc in DIR_HASH.items():

        nr, nc = r + rc[0], c + rc[1]
        if not (0 <= nr < len(arr) and 0 <= nc < len(arr[0])):
            continue

        next_pipe = arr[nr][nc]
        if next_pipe in CURR_PIPES and DIR_REV[d] in CURR_PIPES[next_pipe]:
            pipe_dir.append(d)

    if len(pipe_dir) != 2:
        raise Exception(f"expect only 2 direction received {pipe_dir}")

    for p, d in CURR_PIPES.items():
        if all([dirs in pipe_dir for dirs in d]):
            return p


def transverse_pipe(arr: list[list[str]]):
    """Run through the pipe from starting pos back to starting pos."""
    r, c = get_start_pos(arr)
    curr_pipe = start_pipe_shape((r, c), arr)
    visited = []

    loop_found = False
    while not loop_found:
        for d in CURR_PIPES[curr_pipe]:
            rc = DIR_HASH[d]
            nr, nc = r + rc[0], c + rc[1]

            if not (0 <= nr < len(arr) and 0 <= nc < len(arr[0])):
                continue

            if (nr, nc) not in visited:
                curr_pipe = arr[nr][nc]

                visited.append((r, c))
                r, c = nr, nc
                break

        else:
            print("reached the loop")
            visited.append((r, c))
            loop_found = True
    return visited


def pick_and_shoelace(visited: list[tuple[int, int]]):
    """using reddit's suggestion for the combinatin of 2 formula.

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
    b = len(visited)
    i = area - (b / 2) + 1

    return i


@utils.timer
def main(data):

    visited = transverse_pipe(data)
    part_1 = len(visited) // 2
    part_2 = pick_and_shoelace(visited)

    return part_1, part_2


if __name__ == "__main__":

    data = utils.get_data(10)
    part_1, part_2 = main(data)

    utils.print_solution(2023, 10, "Part 1", part_1)
    utils.print_solution(2023, 10, "Part 2", part_2)
