"""Main Entry point for Advent of Code Solutions."""

import importlib
import os
from pathlib import Path

import requests
import typer
from dotenv import load_dotenv
from rich.console import Console
from typing_extensions import Annotated

import utils

load_dotenv()
CONFIG = {"work_dir": Path.cwd(), "data_dir": "./data"}

app = typer.Typer(
    help="CLI for Advent of Code management over multiple years.",
    no_args_is_help=True,
)

console = Console()


def valid_year(year: int):
    """Check that year is within AOC calendar limits, from 2015 onwards."""
    import datetime

    year_now = datetime.datetime.now().year
    return 2015 <= year < year_now


@app.command()
def create(year: int):
    """Create folder and respective py files for selected year.

    Args:
        year (int): YEAR in YYYY format
    """
    if not valid_year(year):
        console.print(f"Year {year} is not available in AOC events", style="red")
        return
    work_dir = CONFIG["work_dir"]
    console.print(f"Creating folder for {year} in {work_dir}", style="bold")
    year_folder = Path(work_dir, str(year))

    if year_folder.is_dir():
        console.print("Folder alrdy exist, skipping..", style="red")
        return

    console.print(f"creating folder {year} and the days file...", style="italic green")
    year_folder.mkdir()

    Path(year_folder, "__init__.py").touch()

    for i in range(1, 26):
        code_template = utils.main_code_template(i, year=year)
        day_file = Path(year_folder, f"day_{i:02d}.py")
        if not day_file.is_file():
            with open(day_file.as_posix(), mode="w") as file:
                file.write(code_template)
        else:
            console.print("File alrdy exist, skipping..", style="red")


@app.command()
def retrieve(
    year: int,
    day: int,
    overwrite: Annotated[
        bool, typer.Option("-o", help="Retrieve and Overwrite exisiting data")
    ] = False,
):
    """
    Retrieve AOC data from provided year and day.

    Test data needs manual copy and pasting though...

    Args:
        year (int): Year of the AOC
        day (int): Which day of the AOC
    """
    console.print(f"Retrieving data from YEAR {year} and DAY {day}", style="blue")

    data_dir = CONFIG["data_dir"]
    year_path = Path(data_dir, str(year))
    year_path.mkdir(parents=True, exist_ok=True)

    day_txt = Path(year_path, f"input_{day:02d}.txt")
    day_test_txt = Path(year_path, f"test_input_{day:02d}.txt")

    if day_txt.is_file() and not overwrite:
        console.print(f"{day_txt} already exists.", style="blue")
        return

    if not day_test_txt.is_file() or overwrite:
        day_test_txt.touch()

    try:
        resp = requests.get(
            url=f"https://adventofcode.com/{year}/day/{day}/input",
            headers={
                "User-Agent": os.getenv("USER_AGENT"),
                "Cookie": os.getenv("SESSION"),
            },
        )
        if resp.status_code >= 400:
            console.print(f"Error {resp} occured")
            return
    except Exception as e:
        console.print(f"Error in requesting data {e=}", style="bold red")
        return

    with open(day_txt.as_posix(), mode="w") as f:
        f.write(resp.text)

    console.print(
        f"Successfully retrieve {year}/{day:02d} data."
        f"Please manually copy and paste test data in created {day_test_txt.name} file"
    )
    return


@app.command()
def run(
    year: int,
    day: int,
    test: Annotated[bool, typer.Option("-s", help="Use actual data to run")] = True,
):
    """
    Run and output actual data against the solution. Manually submit it in website.

    Submiited solution is cached in folder if duplicate exists.

    Args:
        year (int): Year of the AOC
        day (int): Which day of the AOC
    """
    solve = importlib.import_module(f"{year}.day_{day:02d}")
    if test:
        console.print(f"Testing {year} and {day}", style="blue bold")

    data = utils.get_data(day, test_data=test)
    p1, p2 = solve.main(data)

    utils.print_solution(year, day, "Part 1", p1)
    utils.print_solution(year, day, "Part 2", p2)


if __name__ == "__main__":
    app()
