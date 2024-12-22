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
    """
    using test set as
    1
    2
    3
    2024
    as part of part 2 sample for part 1.
    """
    part1, part2 = MAIN.main(data)

    assert part1 == 37990510
    assert part2 == 23
