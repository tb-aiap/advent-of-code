"""Test for day 19 inputs."""

import pytest

from day_19 import main
from utils import get_data


@pytest.fixture()
def data():
    return get_data(19, test_data=True)


def test_main(data):
    part1, part2 = main(data)

    # You can modify these assertions based on the actual expected values for the day
    assert part1 == 6
    assert part2 == 16
