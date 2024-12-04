"""Solution for day 4 2024 in Python."""

DAY_NO = __file__.rsplit("_", maxsplit=1)[-1].rstrip(".py")

with open(f"data/input_{DAY_NO}.txt", "r") as f:
    data = [s.strip() for s in f]

WORD = "XMAS"

# Part 1 Solution


class PuzzleFinder:
    def __init__(self, puzzle: list[str]):
        self.puzzle = puzzle
        self.row_len = len(puzzle)
        self.col_len = len(puzzle[0])
        self.target = WORD
        self.target_len = len(self.target)

    def _validate_up_limit(self, r):
        return r - self.target_len + 1 < 0

    def _validate_down_limit(self, r):
        return r + self.target_len > self.row_len

    def _validate_right_limit(self, c):
        return c + self.target_len > self.col_len

    def _validate_left_limit(self, c):
        return c - self.target_len + 1 < 0

    def search_right(self, r: int, c: int) -> bool:
        """Search right for XMAS."""

        if self._validate_right_limit(c):
            return 0

        chain = 1
        for i in range(1, self.target_len):
            next_col = c + i
            if chain < 4 and self.puzzle[r][next_col] == self.target[i]:
                chain += 1
            else:
                break

        return 1 if chain == 4 else 0

    def search_left(self, r: int, c: int) -> bool:
        """Search left for SMA'X'."""

        if self._validate_left_limit(c):
            return 0

        chain = 1
        for i in range(1, self.target_len):
            next_col = c - i
            if chain < 4 and self.puzzle[r][next_col] == self.target[i]:
                chain += 1
            else:
                break

        return 1 if chain == 4 else 0

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
            if chain < 4 and self.puzzle[next_row][c] == self.target[i]:
                chain += 1
            else:
                break

        return 1 if chain == 4 else 0

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
            if chain < 4 and self.puzzle[next_row][c] == self.target[i]:
                chain += 1
            else:
                break

        return 1 if chain == 4 else 0

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
            if chain < 4 and self.puzzle[next_row][next_col] == self.target[i]:
                chain += 1
            else:
                break

        return 1 if chain == 4 else 0

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
            if chain < 4 and self.puzzle[next_row][next_col] == self.target[i]:
                chain += 1
            else:
                break

        return 1 if chain == 4 else 0

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
            if chain < 4 and self.puzzle[next_row][next_col] == self.target[i]:
                chain += 1
            else:
                break

        return 1 if chain == 4 else 0

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
            if chain < 4 and self.puzzle[next_row][next_col] == self.target[i]:
                chain += 1
            else:
                break

        return 1 if chain == 4 else 0


if __name__ == "__main__":

    finder = PuzzleFinder(data)

    result = 0
    for r, s in enumerate(data):
        for c, ss in enumerate(s):
            if ss == "X":
                result += finder.search_right(r, c)
                result += finder.search_left(r, c)
                result += finder.search_down(r, c)
                result += finder.search_up(r, c)
                result += finder.search_diagonal_right_down(r, c)
                result += finder.search_diagonal_left_down(r, c)
                result += finder.search_diagonal_right_up(r, c)
                result += finder.search_diagonal_left_up(r, c)

    print("Answer for part 1", result)
