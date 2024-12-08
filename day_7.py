"""Solution for Day 7."""

from utils import get_data, timer


def split_data(data: list[str]) -> tuple[int, int]:

    ans = []
    inputs = []
    for s in data:
        a, i = s.split(":")
        ans.append(int(a.strip()))
        inputs.append(list(map(int, i.strip().split(" "))))

    return ans, inputs


def brute_force_recursive(left, arr: list[int], ans, concat: bool = False):

    if not arr:
        return left == ans
    elif left > ans:
        return False

    right = arr[0]
    remaining_arr = arr[1:]

    if concat:
        concatenate = brute_force_recursive(
            int(str(left) + str(right)), remaining_arr, ans, concat=concat
        )

    adding = brute_force_recursive(left + right, remaining_arr, ans, concat=concat)
    multiply = brute_force_recursive(left * right, remaining_arr, ans, concat=concat)

    return adding or multiply or (concatenate if concat else False)


@timer
def main(data):

    ans, qns = split_data(data)
    result = 0
    part_2 = 0
    for i in range(len(qns)):
        if brute_force_recursive(qns[i][0], qns[i][1:], ans[i]):
            result += ans[i]

        elif brute_force_recursive(qns[i][0], qns[i][1:], ans[i], concat=True):
            part_2 += ans[i]

    return result, result + part_2


if __name__ == "__main__":

    data = get_data(day_no=7)
    part_1, part_2 = main(data)

    print("Solution for Part 1", part_1)
    print("Solution for Part 2", part_2)
