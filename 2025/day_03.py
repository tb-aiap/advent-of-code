"""Solution for Day 3 2025."""

import utils


def find_max_combi(bank):

    max_jolt = 0
    for i in range(len(bank)):
        for j in range(i + 1, len(bank)):
            result = int(bank[i] + bank[j])
            max_jolt = max(max_jolt, result)
    return max_jolt


def find_max_combi_2(bank):
    target_length = 12
    remaining_combi = target_length
    result = ""
    while len(result) < 12:
        bank_last_idx = len(bank)

        for i in range(9, 0, -1):
            if str(i) not in bank:
                continue
            target = bank.index(str(i))
            if remaining_combi < bank_last_idx - target:
                result += bank[target]
                remaining_combi -= 1
                bank = bank[target + 1 :]
                break
            elif target + remaining_combi == bank_last_idx:
                result += bank[target:]
                return int(result)

    return int(result)


@utils.timer
def main(data):

    part_1 = sum(find_max_combi(bank) for bank in data)
    part_2 = sum(find_max_combi_2(bank) for bank in data)

    return part_1, part_2


if __name__ == "__main__":

    data = utils.get_data(3)
    part_1, part_2 = main(data)

    utils.print_solution(2025, 3, "Part 1", part_1)
    utils.print_solution(2025, 3, "Part 2", part_2)
