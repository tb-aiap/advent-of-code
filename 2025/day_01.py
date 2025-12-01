"""Solution for Day 1 2025."""

import utils


def solve(data, part2=False):
    curr = 50
    zero_counter = 0

    for combi in data:
        d, steps = combi[0], int(combi[1:])

        loop_times = steps // 100
        if loop_times > 0 and part2:
            zero_counter += loop_times

        steps = steps % 100
        if d == "R":
            next_curr = (steps + curr) % 100

            if next_curr > 0 and next_curr < curr and part2:
                zero_counter += 1

        if d == "L":
            next_curr = curr - steps
            if next_curr < 0:
                next_curr += 100
                if part2 and curr > 0:
                    zero_counter += 1

        curr = next_curr
        if curr == 0:
            zero_counter += 1

    return zero_counter


@utils.timer
def main(data):

    part_1 = solve(data)
    part_2 = solve(data, True)

    return part_1, part_2


if __name__ == "__main__":

    data = utils.get_data(1)
    part_1, part_2 = main(data)

    utils.print_solution(2025, 1, "Part 1", part_1)
    utils.print_solution(2025, 1, "Part 2", part_2)
