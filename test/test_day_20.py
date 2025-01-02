"""Test for day 20 inputs."""

import pytest
from utils import get_data
from day_20 import main


@pytest.fixture()
def data():
    return get_data(20, test_data=True)


def test_main(data):
    part1, part2 = main(data)

    # You can modify these assertions based on the actual expected values for the day
    assert part1 == None
    assert part2 == None
