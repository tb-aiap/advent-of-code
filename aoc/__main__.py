import importlib
import sys
from pathlib import Path

import typer
from typing_extensions import Annotated

add_path = Path(__file__, f"../..").resolve()
sys.path.append(add_path.as_posix())

import utils

app = typer.Typer(
    help="CLI for Advent of Code management over multiple years.",
    no_args_is_help=True,
)


@app.command()
def retrieve(year: int, day: int):
    """
    Retrieve AOC data from provided year and day.

    Test data needs manual copy and pasting though...

    Args:
        year (int): Year of the AOC
        day (int): Which day of the AOC
    """
    print(f"Retrieving {year} and {day}")


@app.command()
def run(
    year: int,
    day: int,
    submit: Annotated[bool, typer.Option(help="Use actual data to run")] = False,
):
    """
    Run and output actual data against the solution. Manually submit it in website.

    Submiited solution is cached in folder if duplicate exists.

    Args:
        year (int): Year of the AOC
        day (int): Which day of the AOC
    """

    solve = importlib.import_module(f"{year}.day_{day:02d}")
    print(submit)
    print(f"Testing {year} and {day}")

    data = utils.get_data(day, test_data=submit)
    p1, p2 = solve.main(data)

    utils.print_solution(year, day, "Part 1", p1)
    utils.print_solution(year, day, "Part 2", p2)


if __name__ == "__main__":
    app()
