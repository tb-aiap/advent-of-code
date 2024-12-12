"""Test for day 11 inputs."""

import importlib

import pytest

from utils import get_data

DAY = __file__.rsplit("_", maxsplit=1)[-1].rstrip(".py")


@pytest.fixture()
def data():
    return get_data(DAY, test_data=True)


def test_main_part_1(data):

    test_for_day = importlib.import_module(f"day_{DAY}")
    part1, part2 = test_for_day.main(data)

    assert part1 == 55312
    assert part2 == 65601038650482
