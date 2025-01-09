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

# Part 2
result = re.finditer(r"(mul\(\d*,\d*\))|(don't\(\))|(do\(\))", "".join(data))

answer = 0
mul_flag = True
for r in result:

    parsed_str = r.group(0)

    if parsed_str.startswith("mul") and mul_flag:
        answer += parse_mul_str(parsed_str)

    elif parsed_str.startswith("don't()"):
        mul_flag = False

    elif parsed_str.startswith("do()"):
        mul_flag = True


print("Part 2", answer)
