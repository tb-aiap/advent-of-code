from pathlib import Path

CONFIG_DIR = "./data"


def get_data(day_no: int, test_data: bool = False):
    """Function to get data."""

    is_test = "" if not test_data else "test_"
    file_input = f"{is_test}input_{day_no}.txt"

    input_path = Path(CONFIG_DIR, file_input)

    with open(input_path, "r") as f:
        data = [s.strip() for s in f]

    return data
