"""Solution for day 5 2024 in Python."""

from collections import defaultdict


def get_data(test_data: bool = False):
    """Function to get data."""
    day_no = __file__.split("_", maxsplit=1)[-1].rstrip(".py")
    test_ = "test_" if test_data else ""

    input_path = f"data/{test_}input_{day_no}.txt"

    with open(input_path, "r") as f:
        data = [s.strip() for s in f]

    return data


def parse_page_order(data: list[str]):
    """Split input text into page order and pages to update accordingly."""
    page_order = [s for s in data if "|" in s]
    pages_to_update = [s for s in data if "|" not in s]

    return page_order, pages_to_update


def check_pages_violate_page_order(
    page_arr: list[str],
    page_order_hash: dict[str, list[str]],
):
    """For each page, check the pages before if there are any that violates the list"""
    result_hash = dict()
    for idx, page in enumerate(page_arr):

        page_list = page_order_hash[page]
        pages_before = page_arr[:idx]
        result = [pb for pb in pages_before if pb in page_list]

        result_hash[page] = result

    return result_hash


def main(data):
    """Main function for solution."""
    page_order, pages_to_update = parse_page_order(data)
    page_order_hash = defaultdict(list)
    pages_to_update_arr = [s.split(",") for s in pages_to_update if s]

    for p in page_order:
        left, right = p.split("|")
        page_order_hash[left].append(right)

    middle_pages = []
    incorrect_arr = []
    for p_arr in pages_to_update_arr:

        result_hash = check_pages_violate_page_order(p_arr, page_order_hash)

        if not any(result_hash.values()):
            # Part 1
            middle_pages.append(int(p_arr[len(p_arr) // 2]))
        else:
            # Part 2
            stack = []
            for p in p_arr:

                if stack and result_hash[p]:
                    loc = -len(result_hash[p])
                    stack.insert(loc, p)
                else:
                    stack.append(p)
            incorrect_arr.append(int(stack[len(stack) // 2]))

    part_1 = sum(middle_pages)
    part_2 = sum(incorrect_arr)

    return part_1, part_2


if __name__ == "__main__":

    data = get_data()
    part_1, part_2 = main(data)

    print("Solution for Part 1", part_1)
    print("Solution for Part 2", part_2)
