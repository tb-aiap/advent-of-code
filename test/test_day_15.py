"""Test for day 15 inputs."""

import importlib

import pytest

from utils import get_data

DAY = __file__.rsplit("_", maxsplit=1)[-1].rstrip(".py")
MAIN = importlib.import_module(f"day_{DAY}")


@pytest.fixture()
def data():
    return get_data(DAY, test_data=True)


def test_main(data):

    part1, part2 = MAIN.main(data)

    assert part1 == 10092
    assert part2 == 0
