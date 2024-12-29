"""Solution for Day 17 2024."""

from dataclasses import dataclass, field

import utils

COMBO = {
    0: 0,
    1: 1,
    2: 2,
    3: 3,
    4: "A",
    5: "B",
    6: "C",
}


@dataclass
class ThreeBitComputer:

    program: list[int]
    register: dict[str, int]
    ptr: int = field(default=0)

    def solve(self):

        result = []
        while self.ptr < len(self.program):
            p = self.program[self.ptr]
            c = self.program[self.ptr + 1]
            output = getattr(self, f"opcode_{p}")(c)

            if output is not None:
                result.append(str(output))

            if p != 3:
                self.ptr += 2

        return ",".join(result)

    def get_combo(self, v):

        combo = COMBO.get(v)
        if isinstance(combo, str):
            return self.register[combo]

        elif isinstance(combo, int):
            return combo

        else:
            raise NotImplementedError(f"Combo value {v} results in {combo}")

    def opcode_0(self, v) -> None:
        numerator = self.register["A"]
        denominator = 2 ** self.get_combo(v)
        self.register["A"] = numerator // denominator

        return

    def opcode_1(self, v) -> None:

        self.register["B"] = self.register["B"] ^ v

        return

    def opcode_2(self, v) -> None:

        self.register["B"] = self.get_combo(v) % 8

    def opcode_3(self, v) -> None:
        if self.register["A"] == 0:
            self.ptr += 2
        else:
            self.ptr = v

        return

    def opcode_4(self, v) -> None:

        self.register["B"] = self.register["B"] ^ self.register["C"]

        return

    def opcode_5(self, v):
        "Outputs"
        return self.get_combo(v) % 8

    def opcode_6(self, v):
        numerator = self.register["A"]
        denominator = 2 ** self.get_combo(v)
        self.register["B"] = numerator // denominator

        return

    def opcode_7(self, v):
        numerator = self.register["A"]
        denominator = 2 ** self.get_combo(v)
        self.register["C"] = numerator // denominator

        return


def main(data: list[str]):

    register = dict()
    program = []

    for row in data:
        if row.startswith("Register"):
            register[row.split(" ")[1][0]] = int(row.split(" ")[-1])
        if row.startswith("Program"):
            program = [int(i) for i in row.split(" ")[-1].split(",")]

    prog = ThreeBitComputer(program=program, register=register)
    part_1 = prog.solve()

    print(part_1)

    return part_1, None


if __name__ == "__main__":

    DAY = __file__.rsplit("_", maxsplit=1)[-1].rstrip(".py")
    data = utils.get_data(DAY)
    part_1, part_2 = main(data)

    utils.print_solution(2024, DAY, "Part 1", part_1)
    utils.print_solution(2024, DAY, "Part 2", part_2)
