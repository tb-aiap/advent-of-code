from itertools import islice, tee
from pathlib import Path
from typing import Iterable, Iterator

CONFIG_DIR = "./data"


def get_data(day_no: int, test_data: bool = False):
    """Function to get data."""

    is_test = "" if not test_data else "test_"
    file_input = f"{is_test}input_{day_no}.txt"

    input_path = Path(CONFIG_DIR, file_input)

    with open(input_path, "r") as f:
        data = [s.strip() for s in f]

    return data


def sliding_window(arr: Iterable, length=4) -> Iterator:

    sliced_arr = [islice(it, idx, None) for idx, it in enumerate(tee(arr, length))]

    return zip(*sliced_arr)


def get_last_coord_rectangle(arr: list[tuple[int, int]]) -> tuple[int, int]:
    """Get the last coordinate given 3 paris of input."""
    r_arr = [int(i[0]) for i in arr]
    c_arr = [int(i[1]) for i in arr]

    r = [i for i in r_arr if r_arr.count(i) == 1]
    c = [i for i in c_arr if c_arr.count(i) == 1]

    if len(r) > 1 or len(c) > 1:
        raise ValueError(f"Excepted 1 value of r and c . Received {r}, {c}")
    return r[0], c[0]
