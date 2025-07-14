import typer

app = typer.Typer(help="CLI for Advent of Code management over multiple years.",no_args_is_help=True)

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
def test(year: int, day: int):
    """
    Test AOC sample data for year and day.

    Remember to manually copy and paste the data.

    Args:
        year (int): Year of the AOC
        day (int): Which day of the AOC 
    """
    print(f"Testing {year} and {day}")

@app.command()
def run(year: int, day: int):
    """
    Run and output actual data against the solution. Manually submit it in website.

    Submiited solution is cached in folder if duplicate exists.

    Args:
        year (int): Year of the AOC
        day (int): Which day of the AOC 
    """
    print(f"Testing {year} and {day}")

if __name__ == "__main__":
    app()