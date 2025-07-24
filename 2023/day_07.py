"""Solution for Day 7 2023."""

from collections import Counter

import utils

CARD = {
    "A": 13,
    "K": 12,
    "Q": 11,
    "J": 10,
    "T": 9,
    "9": 8,
    "8": 7,
    "7": 6,
    "6": 5,
    "5": 4,
    "4": 3,
    "3": 2,
    "2": 1,
}

SUITE = {
    "five_kind": 7,
    "four_kind": 6,
    "full_house": 5,
    "three_kind": 4,
    "two_pair": 3,
    "one_pair": 2,
    "high_card": 1,
}


def assign_value(card: str, part_2: bool = False):
    """Convert a card into values based on their positions."""
    if part_2:
        CARD["J"] = 0
    base = 1
    result = 0
    for s in card[::-1]:
        result += CARD[s] * base
        base *= 100

    if part_2 and "J" in card:
        result += SUITE[get_best_suite(card)] * base
    else:
        result += SUITE[get_suite(card)] * base
    return result


def get_suite(card: str) -> str:
    "Identify a card suit"
    c = Counter(card)
    if len(c) == 5:
        return "high_card"
    if len(c) == 4:
        return "one_pair"
    if len(c) == 3:
        if c.most_common(1)[0][1] == 3:
            return "three_kind"
        if c.most_common(1)[0][1] == 2:
            return "two_pair"
        raise Exception(f"two pair or three kind error {c}")
    if len(c) == 2:
        if c.most_common(1)[0][1] == 3:
            return "full_house"
        if c.most_common(1)[0][1] == 4:
            return "four_kind"
        raise Exception(f"full_house or four_kind error {c}")
    if len(c) == 1:
        return "five_kind"

    raise Exception(f"unable to capture a suite {c}")


def get_best_suite(card: str) -> str:
    """Try to replace all J with all possible combination"""
    joker_can_be = "AKQT98765432"
    result = 0
    result_suite = "five_kind"  # assuming JJJJJ
    for j in joker_can_be:
        if j not in card:
            continue
        temp = card
        best_suite = get_suite(temp.replace("J", j))
        if SUITE[best_suite] > result:
            result = SUITE[best_suite]
            result_suite = best_suite
    return result_suite


def solve(data: list[str], part_2: bool = False) -> tuple[tuple[int, int]]:
    """Solution for Day 7."""
    result = []
    for set in data:
        card, bet = set.split(" ")
        result.append((assign_value(card, part_2), bet))

    return sorted(result, key=lambda x: x[0])


@utils.timer
def main(data):

    part_1 = sum(rank * int(result[1]) for rank, result in enumerate(solve(data), 1))
    part_2 = sum(rank * int(r[1]) for rank, r in enumerate(solve(data, part_2=True), 1))

    return part_1, part_2


if __name__ == "__main__":

    data = utils.get_data(7)
    part_1, part_2 = main(data)

    utils.print_solution(2023, 7, "Part 1", part_1)
    utils.print_solution(2023, 7, "Part 2", part_2)
