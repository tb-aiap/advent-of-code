"""Test for day 21 inputs."""

import pytest

from day_21 import main
from utils import get_data


@pytest.fixture()
def data():
    return get_data(21, test_data=True)


def test_main(data):
    part1, part2 = main(data)

    # You can modify these assertions based on the actual expected values for the day
    assert part1 == 126384
    assert part2 == None
