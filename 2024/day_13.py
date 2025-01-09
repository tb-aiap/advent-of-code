"""Solution for Day 13 2024."""

import numpy as np

from utils import get_data, timer

# Cost of coins
COST_A = 3
COST_B = 1
CONVERT = 10000000000000


def _get_coords(move: str, split_sign: str, convert: int) -> tuple[int, int]:

    x, y = move.split(", ")
    if split_sign not in x or split_sign not in y:
        raise ValueError(f"Expecting {split_sign} to be in X and Y movements.")

    x = x.split(split_sign)[1]
    y = y.split(split_sign)[1]

    if split_sign == "=":
        return int(x) + convert, int(y) + convert
    return int(x), int(y)


def parse_data(data: list[str], convert=CONVERT):
    machine_data = dict()
    for d in data:
        if d.startswith("Button A"):
            machine_data["A"] = _get_coords(
                d.split(": ")[-1], split_sign="+", convert=convert
            )
        elif d.startswith("Button B"):
            machine_data["B"] = _get_coords(
                d.split(": ")[-1], split_sign="+", convert=convert
            )
        elif d.startswith("Prize"):
            machine_data["T"] = _get_coords(
                d.split(": ")[-1], split_sign="=", convert=convert
            )
        elif not d:
            yield machine_data
            machine_data = dict()

    # for the last set of data, there is no empty space to loop
    yield machine_data


def play_machine(m: dict[str, tuple[int]]):

    # x + y = target
    eq_1 = [
        [
            m["A"][0],
            m["B"][0],
        ],
        [
            m["A"][1],
            m["B"][1],
        ],
    ]

    eq_2 = [m["T"][0], m["T"][1]]
    ans = np.linalg.solve(eq_1, eq_2)

    if ans[0] < 0 or ans[1] < 0:
        return 0, 0

    x = int(ans[0] + 0.1)
    y = int(ans[1] + 0.1)

    if (
        x * m["A"][0] + y * m["B"][0] == m["T"][0]
        and x * m["A"][1] + y * m["B"][1] == m["T"][1]
    ):
        return x, y

    return 0, 0


@timer
def main(data):

    part_1 = 0
    part_2 = 0
    for m in parse_data(data, 0):
        a, b = play_machine(m)
        part_1 += a * COST_A
        part_1 += b * COST_B

    part_1 = int(round(part_1, 0))

    for m in parse_data(data, CONVERT):
        a, b = play_machine(m)
        part_2 += a * COST_A
        part_2 += b * COST_B

    part_2 = int(round(part_2, 0))

    return part_1, part_2


if __name__ == "__main__":

    data = get_data(13)
    part_1, part_2 = main(data)

    print("Solution for Part 1", part_1)
    print("Solution for Part 2", part_2)
