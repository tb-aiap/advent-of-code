"""Solution for Day 7 2025."""

import re

import utils


def solve(data, part2=False):
    start_pos = data[0].index("S")

    beam_arr_index = [0] * len(data[0])
    beam_arr_index[start_pos] = 1

    split = 0

    for row in data:
        for m in re.finditer("\^", row):
            splitter = m.start()
            if beam_arr_index[splitter] > 0:
                curr_beam = beam_arr_index[splitter]
                if splitter > 0:
                    beam_arr_index[splitter - 1] += curr_beam
                if splitter < len(data[0]):
                    beam_arr_index[splitter + 1] += curr_beam

                beam_arr_index[splitter] = 0
                split += 1

    return split if not part2 else sum(beam_arr_index)


@utils.timer
def main(data):
    part_1 = solve(data)
    part_2 = solve(data, part2=True)

    return part_1, part_2
