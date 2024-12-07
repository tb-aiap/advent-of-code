"""Test for day 6 inputs."""

import pytest

from day_7 import brute_force_recursive_again, main, main_part_2
from utils import get_data

DAY = 7


@pytest.fixture()
def data():
    return get_data(DAY, test_data=True)


def test_brute_force_recursive_again():

    assert brute_force_recursive_again(15, [6], 156)
    assert brute_force_recursive_again(17, [8, 14], 192)
    assert brute_force_recursive_again(6, [8, 6, 15], 7290)


def test_main(data):

    part_1 = main(data)
    assert part_1 == 3749


def test_main_part_2(data):

    ans = main_part_2(data)
    assert ans == 11387
