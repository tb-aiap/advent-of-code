"""Test for day 5 inputs."""

import pytest

from day_5 import get_data, main


@pytest.fixture()
def data():
    return get_data(5, test_data=True)


def test_main(data):

    part_1, part_2 = main(data)

    assert part_1 == 143
    assert part_2 == 123
