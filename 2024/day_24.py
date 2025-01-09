"""Solution for Day 23 2024."""

import itertools
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
    while stack:
        for c in stack:
            wire_a, truth, wire_b, _, wire_r = c.split(" ")

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
        # print(wire_hash)
        # print(x_bits, y_bits)
        # print(int(x_bits, 2), int(y_bits, 2))
        # print(int(x_bits, 2) + int(y_bits, 2))
        target = bin(int(x_bits, 2) + int(y_bits, 2))[2:]

    print("ans:", part_1)
    print("tar:", target)
    # print(final_hash)
    # 1011101111101101010110101000011100100100000110

    # 1011101111101101010110101000011100100100000110
    # 1011101111101110010110101000010100011011100110 - target
    # 1011101111101101010110101000011100011011100110
    # 1011101111101101010110101000010100011011100110
    # 1011101111101110010110101000010100011011100110

    # fmt: off
    # x00 XOR y00 -> z00
    # y00 AND x00 -> jfb (carry 1)

    # y01 XOR x01 -> jjj
    # jjj XOR jfb -> z01
    # y01 AND x01 -> cpp
    # jfb AND jjj -> pss
    # cpp OR pss -> rtc (carry 2)

    # x02 XOR y02 -> fkn
    # rtc AND fkn -> dbr
    # dbr OR vrb -> psp (CARRY 3)
    # x02 AND y02 -> vrb

    # y03 XOR x03 -> fhp
    # fhp AND psp -> vkp
    # ttc OR vkp -> rsk (carry 4)
    # x03 AND y03 -> ttc

    # y04 XOR x04 -> cwp
    # cwp AND rsk -> dmh
    # dmh OR dsn -> tsw (carry 4)
    # x04 AND y04 -> dsn

    # x05 XOR y05 -> wwm
    # tsw AND wwm -> rnk
    # rnk OR mkq -> z05 (wrong)
    # y05 AND x05 -> mkq

    # y06 XOR x06 -> gwg
    # hdt AND gwg -> ncj            (probably hdt wrong)
    #                   wgp OR ncj -> jjg (carry 6)
    # y06 AND x06 -> wgp
    first_pair = "z05", "hdt"

    # y07 XOR x07 -> shj
    # shj AND jjg -> pbk
    # pbk OR sdq -> ggp (carry 7)
    # y07 AND x07 -> sdq

    # x08 XOR y08 -> cjc
    # ggp AND cjc -> wvc
    # wvc OR hrv -> vkd (carry 8)
    # x08 AND y08 -> hrv

    # y09 XOR x09 -> wqr
    # vkd XOR wqr -> gbf (should be z09)
    # vkd AND wqr -> ttm
    # gbf OR ttm -> pdk (carry 9)
    # x09 AND y09 -> z09
    second_pair = "z09", "gbf"

    # third pair on 15th
    # x13 XOR y13 -> fpd
    # sjh AND fpd -> ffq
    # y13 AND x13 -> dct

    # y14 XOR x14 -> hsh
    # hsh XOR gnt -> z14
    # gnt AND hsh -> bkm
    # bkm OR bwr -> fgc (carry 14)
    # y14 AND x14 -> bwr

    # y15 XOR x15 -> jgt
    # fgc XOR ??? -> z15
    # fgc AND ??? -> nwr
    # !!!! OR mht -> carry15
    # nwr OR jgt -> shs (carry 15)
    # y15 AND x15 -> mht

    # this is the correcto ne
    # y15 XOR x15 -> mht
    # fgc XOR mht -> z15
    # fgc AND mht -> nwr
    # nwr OR jgt -> shs (carry 15)
    # y15 AND x15 -> jgt
    third_pair = "mht", "jgt"

    # for fourth pair (z30, nbf)
    # x29 XOR y29 -> mhh
    # qdw XOR mhh -> z29
    # mhh AND qdw -> hdf
    # jnk OR hdf -> nvv (carry 29)
    # y29 AND x29 -> jnk

    # y30 XOR x30 -> dpr
    # dpr XOR nvv -> z30
    # dpr AND nvv -> ??
    # ?? OR kqh -> carry 30
    # y30 AND x30 -> kqh

    # y30 XOR x30 -> dpr
    # dpr XOR nvv -> z30
    # dpr AND nvv -> nbf
    # ?? OR kqh -> carry 30
    # y30 AND x30 -> kqh

    # dpr XOR nvv -> nbf
    # dpr AND nvv -> z30
    # kqh OR nbf -> rrc
    fourth_pair = "z30", "nbf"
    # fmt: on

    part_2 = [j for i in [first_pair, second_pair, third_pair, fourth_pair] for j in i]
    print(",".join(sorted(part_2)))
    return int(part_1, 2), part_2


if __name__ == "__main__":

    data = get_data(24)
    part_1, part_2 = main(data)

    print("Solution for Part 1", part_1)
    print("Solution for Part 2", part_2)
