"""Solution for Day 22 2024."""

from collections import defaultdict

from utils import get_data, timer


def process_1(secret: int) -> int:

    result = secret * 64
    mix = result ^ secret
    prune = mix % 16777216

    return prune


def process_2(secret: int) -> int:

    result = secret // 32
    mix = result ^ secret
    prune = mix % 16777216

    return prune


def process_3(secret: int) -> int:

    result = secret * 2048
    mix = result ^ secret
    prune = mix % 16777216

    return prune


def generate(secret, number):

    result = secret
    for _ in range(number):
        result = process_1(result)
        result = process_2(result)
        result = process_3(result)

    return result


# part 2
def generate_prices_and_changes(secret):

    sequence_set = dict()
    result = secret
    price_change = []
    prices = [result % 10]

    for _ in range(2000):
        result = process_1(result)
        result = process_2(result)
        result = process_3(result)

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
        prices, price_change = generate_prices_and_changes(j)
        seq_added = set()
        for i in range(4, len(price_change)):
            seq = tuple(price_change[i - 4 : i])

            if seq not in seq_added:
                sequence_set[seq].append(prices[i])
                seq_added.add(seq)

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
