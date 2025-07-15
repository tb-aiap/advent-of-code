"""Main Entry point for Advent of Code Solutions."""

import importlib
from pathlib import Path

import typer
from rich.console import Console
from typing_extensions import Annotated

import retrieve_data
import utils

CONFIG = {
    "work_dir": Path.cwd(),
}

app = typer.Typer(
    help="CLI for Advent of Code management over multiple years.",
    no_args_is_help=True,
)

console = Console()


@app.command()
def create(year: int):
    """Create folder and respective py files for selected year.

    Args:
        year (int): YEAR in YYYY format
    """
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
        code_template = retrieve_data.main_code_template(i, year=year)
        day_file = Path(year_folder, f"day_{i:02d}.py")
        if not day_file.is_file():
            with open(day_file.as_posix(), mode="w") as file:
                file.write(code_template)
        else:
            console.print("File alrdy exist, skipping..", style="red")


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
