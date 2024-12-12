from collections import defaultdict

from utils import get_data, timer


def split_stones(s):

    if s == 0:
        return [1]

    if len(str(s)) % 2 == 0:
        str_s = str(s)
        mid = len(str(s)) // 2

        return [int(str_s[:mid]), int(str_s[mid:])]

    return [s * 2024]


@timer
def main(data):

    hash_map = defaultdict(int)

    for s in map(int, data[0].split(" ")):
        hash_map[s] += 1

    for blink in range(1, 76):
        temp_hash = defaultdict(int)

        for k, v in hash_map.items():
            hash_map[k] -= v
            for ss in split_stones(k):
                temp_hash[ss] += v

        for k, v in temp_hash.items():
            hash_map[k] += v

        if blink == 25:
            part_1 = sum(hash_map.values())

    part_2 = sum(hash_map.values())

    return part_1, part_2


if __name__ == "__main__":

    data = get_data(11)

    part_1, part_2 = main(data)

    print("Solution for Part 1", part_1)
    print("Solution for Part 2", part_2)
