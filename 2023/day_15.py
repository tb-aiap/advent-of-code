"""Solution for Day 15 2023."""

import utils


def hash_char(s: str) -> int:
    value = 0
    for c in s:
        value += ord(c)
        value *= 17
        value %= 256
    return value


def part2(label_data: str) -> list[list[str]]:
    box = [[] for _ in range(256)]

    for label in label_data:
        exist = False
        if "=" in label:
            len_name, focal = label.split("=")
            box_number = box[hash_char(len_name)]
            for idx, b in enumerate(box_number):
                if len_name in b:
                    exist = True
                    break
            if exist:
                box_number[idx] = f"{len_name} {focal}"
            else:
                box_number.append(f"{len_name} {focal}")

        if "-" in label:
            len_name = label[:-1]
            box_number = box[hash_char(len_name)]
            for idx, b in enumerate(box_number):
                if len_name in b:
                    exist = True
                    break
            if exist:
                del box_number[idx]

    return box


def calculate(box: list[list[str]]) -> int:
    result = 0
    for bn, b in enumerate(box, 1):
        for pn, p in enumerate(b, 1):
            focal = int(p.split(" ")[-1])
            result += bn * pn * focal

    return result


@utils.timer
def main(data):

    part_1 = sum(hash_char(s) for s in data[0].split(","))
    part_2 = calculate(part2(data[0].split(",")))

    return part_1, part_2


if __name__ == "__main__":

    data = utils.get_data(15)
    part_1, part_2 = main(data)

    utils.print_solution(2023, 15, "Part 1", part_1)
    utils.print_solution(2023, 15, "Part 2", part_2)
