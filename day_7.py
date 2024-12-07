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


def brute_force_recursive(left, arr: list[int], ans):

    if not arr and left != ans:
        return False
    elif left == ans:
        return True

    right = arr[0]
    remaining_arr = arr[1:]

    multiply = brute_force_recursive(left * right, remaining_arr, ans)
    adding = brute_force_recursive(left + right, remaining_arr, ans)

    return adding or multiply


def brute_force_recursive_again(left, arr: list[int], ans):

    if not arr and left != ans:
        return False
    elif left == ans:
        return True

    right = arr[0]
    remaining_arr = arr[1:]

    multiply = brute_force_recursive_again(left * right, remaining_arr, ans)
    adding = brute_force_recursive_again(left + right, remaining_arr, ans)
    concat = brute_force_recursive_again(
        int(str(left) + str(right)), remaining_arr, ans
    )

    return adding or multiply or concat


@timer
def main(data):

    ans, qns = split_data(data)
    result = 0
    for i in range(len(qns)):
        if brute_force_recursive(qns[i][0], qns[i][1:], ans[i]):
            result += ans[i]

    return result


@timer
def main_part_2(data):

    ans, qns = split_data(data)
    result = 0
    for i in range(len(qns)):
        if brute_force_recursive_again(qns[i][0], qns[i][1:], ans[i]):
            result += ans[i]

    return result


if __name__ == "__main__":

    data = get_data(day_no=7)
    part_1 = main(data)
    print("Solution for Part 1", part_1)

    part_2 = main_part_2(data)
    print("Solution for Part 2", part_2)
