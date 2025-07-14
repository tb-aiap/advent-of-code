import typer
from typing_extensions import Annotated

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
    print(submit)
    print(f"Testing {year} and {day}")


if __name__ == "__main__":
    app()
