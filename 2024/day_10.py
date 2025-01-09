from utils import get_data, is_within_bounds, timer


def transverse(r: int, c: int, val: int, visited: set[tuple[int, int]], data):

    if not is_within_bounds((r, c), data):
        return 0

    if val != int(data[r][c]):
        return 0

    elif 9 == int(data[r][c]):
        visited.append((r, c))
        return 1

    next_val = val + 1
    tr_1 = transverse(r - 1, c, next_val, visited, data)
    tr_2 = transverse(r + 1, c, next_val, visited, data)
    tr_3 = transverse(r, c - 1, next_val, visited, data)
    tr_4 = transverse(r, c + 1, next_val, visited, data)

    return tr_1 + tr_2 + tr_3 + tr_4


@timer
def main(data):
    result = 0
    unique = 0
    for r, _ in enumerate(data):
        for c, val in enumerate(data[r]):
            if int(val) == 0:

                visit_top = []
                unique += transverse(r, c, int(val), visit_top, data)
                result += len(set(visit_top))
                del visit_top

    part_1 = result
    part_2 = unique
    return part_1, part_2


if __name__ == "__main__":
    data = get_data(10)

    part_1, part_2 = main(data)

    print("Solution for Part 1", part_1)
    print("Solution for Part 2", part_2)
