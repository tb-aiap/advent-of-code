"""Test for day 9 inputs."""

import pytest

from day_9 import count_free_space, main
from utils import get_data

DAY = 9


@pytest.fixture()
def data():
    return get_data(DAY, test_data=True)


def test_count_free_space():
    chars = [s for s in "00...111"]
    assert count_free_space(2, chars) == 3


def test_main_part_1(data):

    part1, part2 = main(data[0])

    assert part1 == 1928
    assert part2 == 2858
