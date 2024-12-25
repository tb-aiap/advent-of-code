"""Test for day 12 inputs."""

import importlib
from enum import Enum

import pytest

from utils import get_data

DAY = __file__.rsplit("_", maxsplit=1)[-1].rstrip(".py")
MOD = importlib.import_module(f"day_{DAY}")


@pytest.fixture()
def data():
    return get_data(DAY, test_data=True)


@pytest.fixture()
def dir():
    class Direction(Enum):
        # row, col
        UP = (-1, 0)
        DOWN = (1, 0)
        LEFT = (0, -1)
        RIGHT = (0, 1)

    return Direction


# def test_search_perimeter(data, dir):

#     test_for_day = importlib.import_module(f"day_{DAY}")
#     p_1 = test_for_day.count_perimeter_unit(0, 0, dir, data)
#     p_2 = test_for_day.count_perimeter_unit(5, 2, dir, data)
#     p_3 = test_for_day.count_perimeter_unit(1, 2, dir, data)

#     assert p_1 == 2
#     assert p_2 == 3
#     assert p_3 == 0


def test_dfs(data):

    visited = set()
    p_1 = MOD.dfs(4, 7, "C", visited, data)
    assert len(p_1) == 1

    visited = set()
    p_2 = MOD.dfs(0, 6, "C", visited, data)

    assert len(p_2) == 14


def test_main(data):

    test_for_day = importlib.import_module(f"day_{DAY}")
    part1, part2 = MOD.main(data)

    assert part1 == 1930
    assert part2 == 1206
