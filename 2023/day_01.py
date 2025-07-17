"""Solution for Day 1 2023."""

import utils


@utils.timer
def main(data):

    result_1 = 0
    for label in data:
        digits = [char for char in label if char.isnumeric()]
        code = digits[0] + digits[-1]
        result_1 += int(code)

    part_1 = result_1

    # there is "twoone" but one is required
    numbers = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    result_2 = 0
    for label in data:
        i = 0
        digits = ""
        while i < len(label):
            replace_num = False
            # print(i, label[i:])
            if label[i].isnumeric():
                digits += label[i]
                i += 1
            else:
                for key in numbers:
                    if label[i:].startswith(key):
                        digits += str(numbers[key])
                        break
                i += 1

        code = digits[0] + digits[-1]
        result_2 += int(code)
        print(label, code, result_2)
    part_2 = result_2

    return part_1, part_2


if __name__ == "__main__":

    data = utils.get_data(2023, 1)
    part_1, part_2 = main(data)

    utils.print_solution(2023, 1, "Part 1", part_1)
    utils.print_solution(2023, 1, "Part 2", part_2)
