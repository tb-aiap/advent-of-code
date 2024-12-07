"""Test for day 6 inputs."""

import pytest

from day_6 import Direction, check_in_front, main, main_part_2
from utils import get_data

DAY = 6


@pytest.fixture()
def data():
    return get_data(DAY, test_data=True)


def test_check_in_front():

    curr_dir = Direction.UP
    curr_loc = (1, 1)

    next_row, next_col = check_in_front(curr_loc, curr_dir)

    assert next_row == 0
    assert next_col == 1

    curr_dir = Direction.DOWN
    curr_loc = (1, 1)

    next_row, next_col = check_in_front(curr_loc, curr_dir)

    assert next_row == 2
    assert next_col == 1

    curr_dir = Direction.LEFT
    curr_loc = (1, 1)

    next_row, next_col = check_in_front(curr_loc, curr_dir)

    assert next_row == 1
    assert next_col == 0

    curr_dir = Direction.RIGHT
    curr_loc = (1, 1)

    next_row, next_col = check_in_front(curr_loc, curr_dir)

    assert next_row == 1
    assert next_col == 2


def test_main(data):

    part_1 = main(data)
    part_2 = main_part_2(data)

    assert part_1 == 41
    assert part_2 == 6
