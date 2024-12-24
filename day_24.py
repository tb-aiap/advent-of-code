"""Solution for Day 23 2024."""

from collections import defaultdict

from utils import get_data, timer

TRUTH_TABLE = {
    "XOR": lambda a, b: a ^ b,
    "OR": lambda a, b: a or b,
    "AND": lambda a, b: a and b,
}


def build_connections(a, b, truth, wire_hash):

    return TRUTH_TABLE[truth](wire_hash[a], wire_hash[b])


@timer
def main(data: list[str]):

    wire_hash = {
        v[0]: int(v[1]) for v in map(lambda x: x.split(": "), data[: data.index("")])
    }
    connections = data[data.index("") + 1 :]

    stack = connections
    temp_stack = []
    swap_a, swap_b, swap_c, swap_d = True, True, True, True

    r_a, r_b = "dpr", "kqh"
    r_c, r_d = "hsh", "fpd"

    while stack:
        for c in stack:
            wire_a, truth, wire_b, _, wire_r = c.split(" ")

            if wire_r == r_a and swap_a:
                wire_r = r_b
                swap_a = False

            elif wire_r == r_b and swap_b:
                wire_r = r_a
                swap_b = False

            elif wire_r == r_c and swap_c:
                wire_r = r_d
                swap_c = False

            elif wire_r == r_d and swap_d:
                wire_r = r_c
                swap_d = False

            if wire_a in wire_hash and wire_b in wire_hash:
                wire_hash[wire_r] = build_connections(wire_a, wire_b, truth, wire_hash)
            else:
                temp_stack.append(c)

        stack = temp_stack
        temp_stack = []

    part_1 = ""
    x_bits = ""
    y_bits = ""
    # print(sorted(list(wire_hash.keys()), reverse=True))
    # print(wire_hash)
    for z in sorted(list(wire_hash.keys()), reverse=True):
        if z.startswith("z"):
            part_1 += str(wire_hash[z])
        elif z.startswith("x"):
            x_bits += str(wire_hash[z])
        elif z.startswith("y"):
            y_bits += str(wire_hash[z])

    part_2 = None
    print(part_1)
    # print(x_bits, y_bits)
    # print(int(x_bits, 2), int(y_bits, 2))
    # print(int(x_bits, 2) + int(y_bits, 2))
    print(bin(int(x_bits, 2) + int(y_bits, 2))[2:])
    print(bin(int(x_bits, 2) + int(y_bits, 2))[2:] == part_1)
    # 1011101111101101010110101000011100100100000110

    # 1011101111101110010110101000011100100100000110
    # 1011101111101110010110101000010100011011100110 - target

    # 1011101111101110010110101000001100100100000110

    print(5, 4, 3, 2, 1, 0)
    print(1 and 1, 0 and 0, 1 and 1, 1 and 0, 0 and 1, 0 and 0)
    return int(part_1, 2), part_2

    # 001001
    # 101000

    # 1010110


if __name__ == "__main__":

    data = get_data(24)
    part_1, part_2 = main(data)

    print("Solution for Part 1", part_1)
    print("Solution for Part 2", part_2)
