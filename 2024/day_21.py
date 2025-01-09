"""Solution for Day 21 2024."""

import functools
from collections import defaultdict

import utils

DOOR_PAD = [
    ["7", "8", "9"],
    ["4", "5", "6"],
    ["1", "2", "3"],
    ["X", "0", "A"],
]

DIR_PAD = [
    ["X", "^", "A"],
    ["<", "v", ">"],
]

DIR = {
    "UP": "^",
    "DOWN": "v",
    "LEFT": "<",
    "RIGHT": ">",
}


def get_pos(position: str, grid: list[list[str]]) -> tuple[int, int]:
    "Get coordiante for the specific string, S or E"
    for ridx, r in enumerate(grid):
        if position in r:
            cidx = grid[ridx].index(position)
            return ridx, cidx


def number_pad_direction(curr, next_loc):

    col = ""
    row = ""
    dist = (next_loc[0] - curr[0]), (next_loc[1] - curr[1])

    col += (DIR["RIGHT"] if dist[1] > 0 else DIR["LEFT"]) * abs(dist[1])
    row += (DIR["DOWN"] if dist[0] > 0 else DIR["UP"]) * abs(dist[0])

    if curr[0] == 3 and next_loc[1] == 0:
        steps = row + col
    elif curr[1] == 0 and next_loc[0] == 3:
        steps = col + row
    elif "<" in col:
        steps = col + row
    else:
        steps = row + col

    return steps


def keyboard_direction(curr, next_loc):

    col = ""
    row = ""
    dist = (next_loc[0] - curr[0]), (next_loc[1] - curr[1])

    col += (DIR["RIGHT"] if dist[1] > 0 else DIR["LEFT"]) * abs(dist[1])
    row += (DIR["DOWN"] if dist[0] > 0 else DIR["UP"]) * abs(dist[0])

    if next_loc == (1, 0):
        steps = row + col
    elif curr == (1, 0):
        steps = col + row
    elif "<" in col:
        steps = col + row
    else:
        steps = row + col

    return steps


def get_direction(curr, next_loc, pad):

    if len(pad) == 2:
        steps = keyboard_direction(curr, next_loc)
    else:
        steps = number_pad_direction(curr, next_loc)

    return steps


def push_pad(target, pad: list[list[str]]):

    num_pad = functools.partial(get_pos, grid=pad)

    steps = ""
    start = "A"
    curr = num_pad(start)
    for s in target:
        next_loc = num_pad(s)
        steps += get_direction(curr, next_loc, pad) + "A"

        curr = next_loc

    return steps


def recursion(s: str, depth: int, memo):
    if depth == 0:
        return len(s)

    # return result if recorded
    if (s, depth) in memo:
        return memo[(s, depth)]

    result = 0

    # if not recorded, calculate the result and store it
    for seq in s.split("A")[:-1]:
        next_seq = push_pad(seq + "A", DIR_PAD)
        result += recursion(next_seq, depth - 1, memo)

    memo[(s, depth)] = result

    return result


@utils.timer
def main(data):
    part_1_robot_level = 2
    ans_1 = 0

    part_2_robot_level = 25
    ans_2 = 0

    memo = defaultdict(int)
    for num in data:
        door_seq = push_pad(num, DOOR_PAD)
        result_1 = recursion(door_seq, part_1_robot_level, memo)
        complexity_1 = int(num[:-1]) * result_1
        ans_1 += complexity_1

        result_2 = recursion(door_seq, part_2_robot_level, memo)
        complexity_2 = int(num[:-1]) * result_2
        ans_2 += complexity_2

    return ans_1, ans_2


if __name__ == "__main__":

    data = utils.get_data(21)
    part_1, part_2 = main(data)

    utils.print_solution(2024, 21, "Part 1", part_1)
    utils.print_solution(2024, 21, "Part 2", part_2)
