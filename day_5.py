"""Solution for day 5 2024 in Python."""

from collections import defaultdict
from enum import IntEnum

DAY_NO = __file__.rsplit("_", maxsplit=1)[-1].rstrip(".py")

with open(f"data/input_{DAY_NO}.txt", "r") as f:
    data = [s.strip() for s in f]


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
        pages_before = p_arr[:idx]
        result = [pb for pb in pages_before if pb in page_list]

        result_hash[page] = result

    return result_hash


page_order, pages_to_update = parse_page_order(data)

page_order_hash = defaultdict(list)
pages_to_update_arr = [s.split(",") for s in pages_to_update if s]

for p in page_order:
    left, right = p.split("|")
    page_order_hash[left].append(right)


middle_pages = []
incorrect_arr = []
rejected = False
for p_arr in pages_to_update_arr:

    result_hash = check_pages_violate_page_order(p_arr, page_order_hash)
    print(result_hash)
    print(any(result_hash.values()))

    if not any(result_hash.values()):
        middle_pages.append(int(p_arr[len(p_arr) // 2]))

print("Solution for Part 1", sum(middle_pages))

# print(incorrect_arr)
