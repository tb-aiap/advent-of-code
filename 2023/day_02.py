"""Solution for Day 2 2023."""

import functools
import operator

import utils

CUBES = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def solve_1(data):
    """Solution for part 1."""
    game, plays = data.split(":")
    game_no: str = game.split(" ")[1]

    if not game_no.isdigit():
        raise Exception(f"unexpected game_no: {game_no}")

    for each_game in plays.split(";"):
        for each_ball in each_game.split(","):
            # each_ball = " 3 blue"
            num, color = each_ball.strip().split(" ")
            if CUBES[color] - int(num) < 0:
                return False
    return True


def solve_2(data):
    """Solution for part 2."""
    min_cube = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }
    _, plays = data.split(":")

    for each_game in plays.split(";"):
        for each_ball in each_game.split(","):
            num, color = each_ball.strip().split(" ")
            min_cube[color] = max(min_cube[color], int(num))
    # functools to multiple the list of numbers together.
    return functools.reduce(operator.mul, min_cube.values())


@utils.timer
def main(data):

    part_1 = sum(i for i, game in enumerate(data, 1) if solve_1(game))
    part_2 = sum(solve_2(game) for game in data)

    return part_1, part_2
