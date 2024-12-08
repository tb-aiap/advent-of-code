"""Test for day 8 inputs."""

import pytest

from day_8 import (
    calculate_antinode,
    calculate_resonant_harmonic_antinode,
    is_within_bounds,
    main,
)
from utils import get_data

DAY = 8


@pytest.fixture()
def data():
    return get_data(DAY, test_data=True)


def test_calculate_antinode(data):

    points = ((2, 5), (1, 8))

    result = calculate_antinode(*points, data)

    assert result[0] == (3, 2)
    assert result[1] == (0, 11)


def test_point_within_bound(data):

    assert is_within_bounds((1, 1), data)
    assert not is_within_bounds((-1, 1), data)
    assert not is_within_bounds((1, -1), data)
    assert not is_within_bounds((12, 5), data)
    assert not is_within_bounds((11, 12), data)
    assert is_within_bounds((11, 11), data)


def test_main_part_1(data):

    part1, part2 = main(data)

    assert part1 == 14
    assert part2 == 34


def test_calculate_resonant_harmonic_antinode(data):

    points = ((8, 8), (8, 9))

    result = calculate_resonant_harmonic_antinode(*points, data)

    assert len(result) == 12
