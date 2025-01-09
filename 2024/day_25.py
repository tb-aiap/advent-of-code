"""Solution for Day 25, 2024."""

from utils import get_data, timer


def split_lock_key(data: list[str]):

    try:
        empty_row = data.index("")
    except ValueError:
        empty_row = len(data)

    new_data = data[:empty_row]
    remaining_data = data[empty_row + 1 :]
    return new_data, remaining_data


def count_pins(data):
    """
    ['#####', '##.##', '.#.##', '...##', '...#.', '...#.', '.....']
    """
    return [r.count("#") - 1 for r in zip(*data)]


def fit_key_lock(key: list[int], lock: list[int]):

    return [sum(i) for i in zip(key, lock)]


@timer
def main(data):

    remaining_data = data
    key_arr = []
    lock_arr = []
    while remaining_data:
        key_lock, remaining_data = split_lock_key(remaining_data)

        if key_lock[0].startswith("#"):
            lock_arr.append(count_pins(key_lock))
        elif key_lock[0].startswith("."):
            key_arr.append(count_pins(key_lock))
        else:
            raise ValueError(f"Error in parsing, neither key or lock. {key_lock}")

    part_1 = 0
    for k in key_arr:
        for l in lock_arr:
            if max(fit_key_lock(k, l)) <= 5:
                part_1 += 1

    return part_1, None


if __name__ == "__main__":

    data = get_data(25)
    part_1, part_2 = main(data)

    print("Solution for Part 1", part_1)
    print("Solution for Part 2", part_2)
