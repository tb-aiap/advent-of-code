"""Solution for Day 4 2023."""

import utils


def solve_1(game: str):
    """Solution for part 1."""
    _, cards = game.split(":")
    winning, checking = cards.split("|")

    winning_arr = [i.strip() for i in winning.split(" ") if i]
    checking_arr = [i.strip() for i in checking.split(" ") if i]

    return sum(1 for num in checking_arr if num in winning_arr)


def solve_2(all_games):
    """Solution for part 2."""
    copies = [1 for _ in all_games]

    for i, game in enumerate(all_games):
        winning_number = solve_1(game)
        for j in range(i + 1, min(i + winning_number + 1, len(all_games))):
            copies[j] += copies[i]

    return copies


@utils.timer
def main(data):
    part_1 = sum(2 ** (solve_1(game) - 1) if solve_1(game) else 0 for game in data)
    part_2 = sum(solve_2(data))

    return part_1, part_2


if __name__ == "__main__":

    data = utils.get_data(4)
    part_1, part_2 = main(data)

    utils.print_solution(2023, 4, "Part 1", part_1)
    utils.print_solution(2023, 4, "Part 2", part_2)
