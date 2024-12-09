from collections import deque
from itertools import chain

from utils import get_data, timer


def parse_block(data: str):

    for idx, char in enumerate(data):
        char = int(char)
        if idx % 2:
            output = ["."] * char
        else:
            if char == 0:
                raise ValueError(f"File at index {idx} is size {char}")

            file_id = idx // 2
            output = [file_id] * char

        yield output


def count_free_space(l_index, arr):
    count_idx = l_index
    while arr[count_idx] == ".":
        count_idx += 1

    return count_idx - l_index


@timer
def main(data):

    expand_file = list(parse_block(data))
    expand_arr = list(chain.from_iterable(expand_file))

    l = 0
    r = len(expand_arr) - 1
    while l < r:

        if expand_arr[l] == "." and expand_arr[r] != ".":
            expand_arr[l] = expand_arr[r]
            expand_arr[r] = "."
            l += 1
            r -= 1
        elif expand_arr[l] != ".":
            l += 1
        elif expand_arr[r] == ".":
            r -= 1

    part_1 = sum([i * idx for idx, i in enumerate(expand_arr) if i != "."])

    # Part 2
    expand_arr = list(chain.from_iterable(expand_file))
    l = 0
    r = len(expand_arr) - 1

    while l < r:

        # print("Idx", r, expand_arr[r])
        if expand_arr[r] != ".":
            space_needed = expand_arr.count(expand_arr[r])

            l = 0
            while l < r and space_needed > count_free_space(l, expand_arr):
                l += 1

            if space_needed <= count_free_space(l, expand_arr):

                expand_arr[l : l + space_needed] = expand_arr[
                    r - space_needed + 1 : r + 1
                ]
                expand_arr[r - space_needed + 1 : r + 1] = ["."] * space_needed
                r = r - space_needed

            else:
                l = expand_arr.index(".")
                r = r - space_needed
                space_needed = 0

        elif expand_arr[r] == ".":
            r -= 1

    # print(expand_arr, len(expand_arr))
    part_2 = sum([i * idx for idx, i in enumerate(expand_arr) if i != "."])

    return part_1, part_2


if __name__ == "__main__":

    data = get_data(9)[0]
    part_1, part_2 = main(data)

    print("Solution for Part 1", part_1)
    print("Solution for Part 2", part_2)
