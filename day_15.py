"""Solution for Day 15 2024."""

import pprint

from utils import Direction, get_data, print_solution

DIR = {
    "^": Direction.UP,
    "v": Direction.DOWN,
    "<": Direction.LEFT,
    ">": Direction.RIGHT,
}


def check_in_front(curr_pos: tuple[int], curr_dir: Direction):

    r, c = curr_pos
    row_dir, col_dir = curr_dir.value
    next_row, next_col = r + row_dir, c + col_dir

    return next_row, next_col


def get_guard_pos(grid):
    guard_pos = [(idx, i.index("@")) for idx, i in enumerate(grid) if "@" in i][0]
    return guard_pos


def move_in_front(curr_pos: tuple[int], curr_dir: Direction, grid: list[list[str]]):

    r, c = curr_pos[0], curr_pos[1]
    stack = [(r, c)]
    while stack and grid[r][c] != "#":
        r, c = check_in_front((r, c), curr_dir)
        print(stack, r, c)
        if grid[r][c] == ".":
            while stack:
                sr, sc = stack.pop()
                grid[r][c] = grid[sr][sc]
                grid[sr][sc] = "."
                r, c = sr, sc
        else:
            stack.append((r, c))

    return grid


def can_move_upsize(curr_pos: tuple[int], curr_dir: Direction, grid: list[list[str]]):

    r, c = curr_pos[0], curr_pos[1]
    if grid[r][c] == "#":
        return 1

    if grid[r][c] == "]":
        print("realign r, c")
        # align it to left '[' if its right ']'
        c = c - 1

    lr, lc = check_in_front((r, c), curr_dir)
    rr, rc = check_in_front((r, c + 1), curr_dir)

    print("can move 2")
    print(grid[r][c], r, c, curr_pos)
    print(grid[lr][lc], lr, lc, curr_pos)
    print(grid[rr][rc], rr, rc, curr_pos)
    print()

    if grid[lr][lc] == "." and grid[rr][rc] == ".":
        return 0
    elif grid[lr][lc] == "#" or grid[rr][rc] == "#":
        return 1

    a = 0
    if grid[lr][lc] in "[]":
        a += can_move_upsize((lr, lc), curr_dir, grid)

    if grid[rr][rc] in "[]":
        a += can_move_upsize((rr, rc), curr_dir, grid)

    return a


def move_upsize_up_down(
    curr_pos: tuple[int], curr_dir: Direction, grid: list[list[str]]
):
    print(move_upsize_up_down.__name__, curr_dir, curr_pos)

    r, c = curr_pos[0], curr_pos[1]
    if grid[r][c] == "]":
        # align it to left '[' if its right ']'

        c = c - 1

    lr, lc = check_in_front((r, c), curr_dir)
    rr, rc = check_in_front((r, c + 1), curr_dir)
    if grid[lr][lc] in "[]":
        move_upsize_up_down((lr, lc), curr_dir, grid)

    if grid[rr][rc] in "[]":
        move_upsize_up_down((rr, rc), curr_dir, grid)

    # print("moving parts", grid[nr][nc], grid[nr][nc + 1], grid[nr][nc - 1])
    print("shifting", move_upsize_up_down.__name__, (lr, lc), (r, c))
    # print(r, c, nr, nc)
    if grid[lr][lc] == "." and grid[rr][rc] == ".":
        grid[lr][lc] = grid[r][c]
        grid[r][c] = "."

        grid[rr][rc] = grid[r][c + 1]
        grid[r][c + 1] = "."

    return grid


def upsize(row: str):

    row = (
        row.replace("#", "##").replace(".", "..").replace("O", "[]").replace("@", "@.")
    )
    return row


def print_grid(grid):

    for r in grid:
        print("".join(r))


def main(data):
    grid = [[j for j in i] for i in data[: data.index("")]]
    moves = "".join(data[data.index("") + 1 :])

    guard_pos = [(idx, i.index("@")) for idx, i in enumerate(grid) if "@" in i][0]

    for d in moves:
        grid = move_in_front(guard_pos, DIR[d], grid)
        guard_pos = get_guard_pos(grid)

    part_1 = 0
    for ridx, _ in enumerate(grid):
        for cidx, _ in enumerate(grid[ridx]):
            if grid[ridx][cidx] == "O":
                part_1 += (100 * ridx) + cidx

    # PART 2 - second warehouse
    grid = [[j for j in upsize(i)] for i in data[: data.index("")]]
    guard_pos = [(idx, i.index("@")) for idx, i in enumerate(grid) if "@" in i][0]
    print("Part 2")
    print_grid(grid)
    for d in moves[:]:
        print("MOVE", d)

        if d in "<>":
            print("moving", d)
            grid = move_in_front(guard_pos, DIR[d], grid)
            # guard_pos = get_guard_pos(grid)
        else:
            in_front_coord = check_in_front(guard_pos, DIR[d])
            print("G", guard_pos, "F", in_front_coord)
            if grid[in_front_coord[0]][in_front_coord[1]] == ".":
                grid[guard_pos[0]][guard_pos[1]] = "."
                grid[in_front_coord[0]][in_front_coord[1]] = "@"

            elif can_move_upsize(in_front_coord, DIR[d], grid) == 0:
                print("CAN MOVE", d)
                grid = move_upsize_up_down(in_front_coord, DIR[d], grid)
                # print_grid(grid)
                grid[guard_pos[0]][guard_pos[1]] = "."
                grid[in_front_coord[0]][in_front_coord[1]] = "@"

            else:
                print("CANNOT MOVE", d)
                # print_grid(grid)
                ...
        guard_pos = get_guard_pos(grid)

        # validating pushes
        for row in grid:
            join_row = "".join(row)
            if (
                "[." in join_row
                or ".]" in join_row
                or "@]" in join_row
                or "[@" in join_row
            ):
                raise ValueError()

    part_2 = 0
    print_grid(grid)
    for ridx, _ in enumerate(grid):
        for cidx, _ in enumerate(grid[ridx]):
            if grid[ridx][cidx] == "[":
                part_2 += (100 * ridx) + cidx

    return part_1, part_2


if __name__ == "__main__":

    data = get_data(15)
    part_1, part_2 = main(data)

    print_solution(2024, 15, "Part 1", part_1)
    print_solution(2024, 15, "Part 2", part_2)
