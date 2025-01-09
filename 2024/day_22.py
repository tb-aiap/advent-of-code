"""Solution for Day 22 2024."""

import operator
from collections import defaultdict

from utils import get_data, sliding_window, timer

PROCESS_1 = 64
PROCESS_2 = 32
PROCESS_3 = 2048
PRUNE = 16777216


def process(secret: int, operation, number) -> int:

    result = operation(secret, number)
    mix = result ^ secret
    prune = mix % PRUNE

    return prune


def generate(secret, number):

    result = secret
    for _ in range(number):
        result = process(result, operator.mul, PROCESS_1)
        result = process(result, operator.floordiv, PROCESS_2)
        result = process(result, operator.mul, PROCESS_3)

    return result


# part 2
def generate_prices_and_changes(secret):

    result = secret
    price_change = []
    prices = [result % 10]

    for _ in range(2000):
        result = process(result, operator.mul, PROCESS_1)
        result = process(result, operator.floordiv, PROCESS_2)
        result = process(result, operator.mul, PROCESS_3)

        single_digit = result % 10
        price_change.append(single_digit - prices[-1])
        prices.append(single_digit)

    return prices, price_change


@timer
def main(data):

    part_1 = sum(generate(i, 2000) for i in map(int, data))

    # part 2
    sequence_set = defaultdict(list)

    for j in map(int, data):
        seq_added = set()
        prices, price_change = generate_prices_and_changes(j)

        for idx, sw in enumerate(map(tuple, sliding_window(price_change, 4)), 4):
            if sw not in seq_added:
                sequence_set[sw].append(prices[idx])
                seq_added.add(sw)

    part_2 = sum(max(sequence_set.values(), key=sum))

    return part_1, part_2


if __name__ == "__main__":

    data = get_data(22)
    part_1, part_2 = main(data)

    print("Solution for Part 1", part_1)
    print("Solution for Part 2", part_2)

"""
Note:
    Learn how to optimized the data structure for part 2


"""
