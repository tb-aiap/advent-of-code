import re


def parse_mul_str(mul_str: str):
    result = mul_str.strip("mul()").split(",")
    int_result = [int(i) for i in result]
    multiply = int_result[0] * int_result[1]
    return multiply


with open("data/input_3.txt", "r") as f:
    data = f.readlines()


result = re.findall(r"mul\(\d*,\d*\)", "".join(data))

print("Part 1", sum(map(parse_mul_str, result)))
