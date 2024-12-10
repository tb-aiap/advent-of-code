"""Test for day 10 inputs."""

import pytest

from day_10 import main
from utils import get_data

DAY = __file__.rsplit("_", maxsplit=1)[-1].rstrip(".py")


@pytest.fixture()
def data():
    return get_data(DAY, test_data=True)


def test_main_part_1(data):

    part1, part2 = main(data)

    assert part1 == 36
    assert part2 == 81
