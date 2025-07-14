"""Main Entry point for Advent of Code Solutions."""

import argparse
import importlib

from rich.console import Console

import utils

console = Console()

def get_argparse() -> argparse.ArgumentParser:
    """Parse the required arguments for AOC solutions."""
    parser = argparse.ArgumentParser(description="Advent of Code CLI Options")
    parser.add_argument("-t", default=False, action=argparse.BooleanOptionalAction)
    parser.add_argument("year", type=int)
    parser.add_argument("day", type=int)

    return parser


def main(parser: argparse.ArgumentParser) -> None:
    """Main Entry point to AOC."""
    args = parser.parse_args()
    year = args.year
    day = args.day
    test_data = args.t

    if test_data:
        console.print("Running Test Data", style="bold blue")

    solve = importlib.import_module(f"{year}.day_{day:02d}")

    data = utils.get_data(day, test_data=test_data)
    p1, p2 = solve.main(data)

    utils.print_solution(year, day, "Part 1", p1)
    utils.print_solution(year, day, "Part 2", p2)


if __name__ == "__main__":

    parser = get_argparse()
    main(parser)
