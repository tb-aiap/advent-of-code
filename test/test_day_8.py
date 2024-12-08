"""Test for day 8 inputs."""

import pytest

from day_8 import calculate_antinode, main, point_within_bound
from utils import get_data

DAY = 8


@pytest.fixture()
def data():
    return get_data(DAY, test_data=True)


def test_calculate_antinode():

    data = ((2, 5), (1, 8))

    anti_1, anti_2 = calculate_antinode(*data)

    assert anti_1 == (3, 2)
    assert anti_2 == (0, 11)


def test_point_within_bound(data):

    assert point_within_bound((1, 1), data)
    assert not point_within_bound((-1, 1), data)
    assert not point_within_bound((1, -1), data)
    assert not point_within_bound((12, 5), data)
    assert not point_within_bound((11, 12), data)
    assert point_within_bound((11, 11), data)


def test_main_part_1(data):

    part1 = main(data)

    assert part1 == 14
