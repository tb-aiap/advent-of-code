"""Test for day 7 inputs."""

import pytest

from day_7 import main
from utils import get_data

DAY = 7


@pytest.fixture()
def data():
    return get_data(DAY, test_data=True)


def test_main(data):

    part_1, part_2 = main(data)
    assert part_1 == 3749
    assert part_2 == 11387


# def test_main_part_2(data):

#     ans = main_part_2(data)
#     assert ans == 11387
