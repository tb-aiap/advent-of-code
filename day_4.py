"""Solution for day 4 2024 in Python."""

from collections import defaultdict

DAY_NO = __file__.rsplit("_", maxsplit=1)[-1].rstrip(".py")

with open(f"data/input_{DAY_NO}.txt", "r") as f:
    data = [s.strip() for s in f]


# Part 1 Solution
class PuzzleFinder:
    def __init__(self, puzzle: list[str], target: str):
        self.puzzle = puzzle
        self.row_len = len(puzzle)
        self.col_len = len(puzzle[0])
        self.target = target
        self.target_len = len(self.target)

    def _validate_up_limit(self, r):
        return r - self.target_len + 1 < 0

    def _validate_down_limit(self, r):
        return r + self.target_len > self.row_len

    def _validate_right_limit(self, c):
        return c + self.target_len > self.col_len

    def _validate_left_limit(self, c):
        return c - self.target_len + 1 < 0

    def _return_valid_count(self, chain):
        return 1 if chain == self.target_len else 0

    def search_right(self, r: int, c: int) -> bool:
        """Search right for XMAS."""

        if self._validate_right_limit(c):
            return 0

        chain = 1
        for i in range(1, self.target_len):
            next_col = c + i
            if chain < self.target_len and self.puzzle[r][next_col] == self.target[i]:
                chain += 1
            else:
                break

        return self._return_valid_count(chain)

    def search_left(self, r: int, c: int) -> bool:
        """Search left for SMA'X'."""

        if self._validate_left_limit(c):
            return 0

        chain = 1
        for i in range(1, self.target_len):
            next_col = c - i
            if chain < self.target_len and self.puzzle[r][next_col] == self.target[i]:
                chain += 1
            else:
                break

        return self._return_valid_count(chain)

    def search_down(self, r: int, c: int) -> bool:
        """Search down for
        X
        M
        A
        S.
        """

        if self._validate_down_limit(r):
            return 0

        chain = 1
        for i in range(1, self.target_len):
            next_row = r + i
            if chain < self.target_len and self.puzzle[next_row][c] == self.target[i]:
                chain += 1
            else:
                break

        return self._return_valid_count(chain)

    def search_up(self, r: int, c: int) -> bool:
        """Search down for
        S
        A
        M
        X.
        """

        if self._validate_up_limit(r):
            return 0

        chain = 1
        for i in range(1, self.target_len):
            next_row = r - i
            if chain < self.target_len and self.puzzle[next_row][c] == self.target[i]:
                chain += 1
            else:
                break

        return self._return_valid_count(chain)

    def search_diagonal_right_down(self, r: int, c: int) -> bool:
        """Search diagonal down for
        X...
        .M..
        ..A.
        ....S
        """

        if self._validate_right_limit(c) or self._validate_down_limit(r):
            return 0

        chain = 1
        for i in range(1, self.target_len):
            next_row = r + i
            next_col = c + i
            if (
                chain < self.target_len
                and self.puzzle[next_row][next_col] == self.target[i]
            ):
                chain += 1
            else:
                break

        return self._return_valid_count(chain)

    def search_diagonal_left_down(self, r: int, c: int) -> bool:
        """Search diagonal down for
        ...X
        ..M.
        .A..
        S...
        """

        if self._validate_left_limit(c) or self._validate_down_limit(r):
            return 0

        chain = 1
        for i in range(1, self.target_len):
            next_row = r + i
            next_col = c - i
            if (
                chain < self.target_len
                and self.puzzle[next_row][next_col] == self.target[i]
            ):
                chain += 1
            else:
                break

        return self._return_valid_count(chain)

    def search_diagonal_right_up(self, r: int, c: int) -> bool:
        """Search diagonal up for
        ...S
        ..A.
        .M..
        X...
        """

        if self._validate_right_limit(c) or self._validate_up_limit(r):
            return 0

        chain = 1
        for i in range(1, self.target_len):
            next_row = r - i
            next_col = c + i
            if (
                chain < self.target_len
                and self.puzzle[next_row][next_col] == self.target[i]
            ):
                chain += 1
            else:
                break

        return self._return_valid_count(chain)

    def search_diagonal_left_up(self, r: int, c: int) -> bool:
        """Search diagonal left up for
        S...
        .A..
        ..M.
        ...X
        """

        if self._validate_left_limit(c) or self._validate_up_limit(r):
            return 0

        chain = 1
        for i in range(1, self.target_len):
            next_row = r - i
            next_col = c - i
            if (
                chain < self.target_len
                and self.puzzle[next_row][next_col] == self.target[i]
            ):
                chain += 1
            else:
                break

        return self._return_valid_count(chain)


class XMasPuzzleFinder(PuzzleFinder):

    def __init__(self, puzzle, target):
        super().__init__(puzzle, target)
        self._validate_target_is_odd()
        self.mid_idx = self.target_len // 2
        self.mid_idx_coord = defaultdict(int)

    def _validate_target_is_odd(self):
        if self.target_len % 2 == 0:
            raise ValueError(f"{__class__} expects odd number length.")

    def search_diagonal_right_down(self, r: int, c: int) -> bool:
        """
        Search diagonal right down for with memory of the middle coordinate.
        M..
        .A.
        ..S
        """

        if self._validate_right_limit(c) or self._validate_down_limit(r):
            return 0

        chain = 1
        for i in range(1, self.target_len):
            next_row = r + i
            next_col = c + i
            if (
                chain < self.target_len
                and self.puzzle[next_row][next_col] == self.target[i]
            ):
                chain += 1
            else:
                break

        if self._return_valid_count(chain):
            mid_row = r + self.mid_idx
            mid_col = c + self.mid_idx
            self.mid_idx_coord[(mid_row, mid_col)] += 1

        return

    def search_diagonal_left_down(self, r: int, c: int) -> bool:
        """
        Search diagonal left down for with memory of the middle coordinate.
        ..M
        .A.
        S..
        """

        if self._validate_left_limit(c) or self._validate_down_limit(r):
            return 0

        chain = 1
        for i in range(1, self.target_len):
            next_row = r + i
            next_col = c - i
            if (
                chain < self.target_len
                and self.puzzle[next_row][next_col] == self.target[i]
            ):
                chain += 1
            else:
                break

        if self._return_valid_count(chain):
            mid_row = r + self.mid_idx
            mid_col = c - self.mid_idx
            self.mid_idx_coord[(mid_row, mid_col)] += 1

        return

    def search_diagonal_right_up(self, r: int, c: int) -> bool:
        """
        Search diagonal right up for with memory of the middle coordinate.
        ..S
        .A.
        M..
        """

        if self._validate_right_limit(c) or self._validate_up_limit(r):
            return 0

        chain = 1
        for i in range(1, self.target_len):
            next_row = r - i
            next_col = c + i
            if (
                chain < self.target_len
                and self.puzzle[next_row][next_col] == self.target[i]
            ):
                chain += 1
            else:
                break

        if self._return_valid_count(chain):
            mid_row = r - self.mid_idx
            mid_col = c + self.mid_idx
            self.mid_idx_coord[(mid_row, mid_col)] += 1

        return

    def search_diagonal_left_up(self, r: int, c: int) -> bool:
        """
        Search diagonal left up for with memory of the middle coordinate.
        S..
        .A.
        ..M
        """

        if self._validate_left_limit(c) or self._validate_up_limit(r):
            return 0

        chain = 1
        for i in range(1, self.target_len):
            next_row = r - i
            next_col = c - i
            if (
                chain < self.target_len
                and self.puzzle[next_row][next_col] == self.target[i]
            ):
                chain += 1
            else:
                break

        if self._return_valid_count(chain):
            mid_row = r - self.mid_idx
            mid_col = c - self.mid_idx
            self.mid_idx_coord[(mid_row, mid_col)] += 1

        return


if __name__ == "__main__":

    WORD = "XMAS"
    finder = PuzzleFinder(data, target=WORD)

    result = 0
    for r, s in enumerate(data):
        for c, ss in enumerate(s):
            if ss == finder.target[0]:
                result += finder.search_right(r, c)
                result += finder.search_left(r, c)
                result += finder.search_down(r, c)
                result += finder.search_up(r, c)
                result += finder.search_diagonal_right_down(r, c)
                result += finder.search_diagonal_left_down(r, c)
                result += finder.search_diagonal_right_up(r, c)
                result += finder.search_diagonal_left_up(r, c)

    print("Answer for part 1", result)

    # Part 2 looking for X-MAS
    # M.S
    # .A.
    # M.S
    MAS = "MAS"
    finder = XMasPuzzleFinder(data, target=MAS)

    result = 0
    for r, s in enumerate(data):
        for c, ss in enumerate(s):
            if ss == finder.target[0]:
                finder.search_diagonal_right_down(r, c)
                finder.search_diagonal_left_down(r, c)
                finder.search_diagonal_right_up(r, c)
                finder.search_diagonal_left_up(r, c)

    print("Answer for part 2", list(finder.mid_idx_coord.values()).count(2))
