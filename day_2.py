"""Solution for day 2 2024."""

MAX_TWO_ADJ_LEVEL = 3
TOLERATE_BAD_LEVEL = 1


def check_increase_safe(arr: list[int]) -> bool:
    """Compare the array for monotonic increasing and difference of 3 max"""

    for i in range(len(arr) - 1):
        diff = abs(arr[i + 1] - arr[i])
        if arr[i] >= arr[i + 1] or diff > MAX_TWO_ADJ_LEVEL:
            return False
    return True


def check_decrease_safe(arr: list[int]) -> bool:
    """Compare the array for monotonic decreasing and difference of 3 max"""

    for i in range(len(arr) - 1):
        diff = abs(arr[i + 1] - arr[i])
        if arr[i] <= arr[i + 1] or diff > MAX_TWO_ADJ_LEVEL:
            return False
    return True


def check_with_dampener(arr: list[int]):
    """For each fail array, try to skip each number and try again."""
    for i in range(len(arr)):
        skip_arr = arr[:i] + arr[i + 1 :]
        if check_increase_safe(skip_arr) or check_decrease_safe(skip_arr):
            return True

    return False


if __name__ == "__main__":

    # Part 1
    with open("data/input_2.txt", "r") as f:
        data = f.readlines()

    result = 0
    for report in data:
        parse_report = report.strip().split(" ")
        parse_report = [int(i) for i in parse_report]

        if any([check_increase_safe(parse_report), check_decrease_safe(parse_report)]):
            result += 1

    print(result)

    # Part 2
    result = 0
    for report in data:
        parse_report = report.strip().split(" ")
        parse_report = [int(i) for i in parse_report]

        if any(
            [
                check_increase_safe(parse_report),
                check_decrease_safe(parse_report),
            ]
        ):
            result += 1
        elif check_with_dampener(parse_report):
            result += 1

    print("Part 2", result)
