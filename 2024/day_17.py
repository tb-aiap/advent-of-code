"""Solution for Day 17 2024."""

from dataclasses import dataclass, field

import utils


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

            output = self.run_program(p, c)
            if output is not None:
                result.append(str(output))

            self.ptr += 2

        return ",".join(result)

    def run_program(self, optcode, value):

        combo = {
            0: 0,
            1: 1,
            2: 2,
            3: 3,
            4: self.register["A"],
            5: self.register["B"],
            6: self.register["C"],
        }

        match optcode:
            case 0:
                self.register["A"] = self.register["A"] // (2 ** combo[value])
            case 1:
                self.register["B"] = self.register["B"] ^ value
            case 2:
                self.register["B"] = combo[value] % 8
            case 3:
                if self.register["A"]:
                    self.ptr = value - 2
            case 4:
                self.register["B"] = self.register["B"] ^ self.register["C"]
            case 5:
                return combo[value] % 8
            case 6:
                self.register["B"] = self.register["A"] // (2 ** combo[value])
            case 7:
                self.register["C"] = self.register["A"] // (2 ** combo[value])

    def solve_mulitple(self):
        """There many various combinations of bits that add up to the desired answer,
        we try various combinations via DFS to get the final result that is the same as program list.

        Returns:
            _type_: _description_
        """
        target = self.program
        stack = [(0, len(self.program) - 1)]
        solution = []
        while stack:
            possible_a, indx = stack.pop()
            for pos in range(8):
                # potential to clean this up wihout using hash map
                candidate = (possible_a * 8) + pos
                self.register["A"] = candidate
                self.register["B"] = 0
                self.register["C"] = 0
                self.ptr = 0

                result = list(map(int, self.solve().split(",")))

                if result == target[indx:]:
                    print(
                        f"Candidate {candidate} match: result {result} = target {target[indx:]}"
                    )
                    next_a = (candidate, indx - 1)
                    stack.append(next_a)

                    if indx == 0:
                        solution.append(candidate)
        print("These are the possible solution", solution)
        print("The minimum is", min(solution))
        return min(solution)


@utils.timer
def main(data: list[str]):

    register = dict()
    program = []

    for row in data:
        if row.startswith("Register"):
            register[row.split(" ")[1][0]] = int(row.split(" ")[-1])
        if row.startswith("Program"):
            program = [int(i) for i in row.split(" ")[-1].split(",")]

    prog = ThreeBitComputer(program=program, register=register.copy())
    part_1 = prog.solve()
    part_2 = prog.solve_mulitple()

    return part_1, part_2


if __name__ == "__main__":

    DAY = __file__.rsplit("_", maxsplit=1)[-1].rstrip(".py")
    data = utils.get_data(DAY)
    part_1, part_2 = main(data)

    utils.print_solution(2024, DAY, "Part 1", part_1)
    utils.print_solution(2024, DAY, "Part 2", part_2)
