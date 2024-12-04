"""Solution for day 4 2024 in Python."""

from collections import defaultdict
from enum import IntEnum

DAY_NO = __file__.rsplit("_", maxsplit=1)[-1].rstrip(".py")

with open(f"data/input_{DAY_NO}.txt", "r") as f:
    data = [s.strip() for s in f]


class Dir(IntEnum):
    """Directions to move in the matrix."""

    # for row direction
    UP = -1
    DOWN = 1

    # for column direction
    LEFT = -1
    RIGHT = 1

    # no direction
    ZERO = 0


# Part 1 Solution
class PuzzleFinder:
    def __init__(self, puzzle: list[str], target: str):
        self.puzzle = puzzle
        self.row_len = len(puzzle)
        self.col_len = len(puzzle[0])
        self.target = target
        self.target_len = len(self.target)

    def _validate_boundaries(
        self,
        r: int,
        c: int,
        row_dir: int,
        col_dir: int,
    ) -> bool:

        r_move = r + row_dir * (self.target_len - 1)
        c_move = c + col_dir * (self.target_len - 1)

        if (0 <= r_move <= self.row_len - 1) and (0 <= c_move <= self.col_len - 1):
            return True

    def _search_direction(
        self,
        r: int,
        c: int,
        row_dir: int,
        col_dir: int,
    ) -> int:
        """Search a specific direction in the n*n matrix.

        Args:
            r (int): Current row index.
            c (int): Current column index.
            row_dir (int): Direction to move. 1 is right, -1 is left, 0 is same index.
            col_dir (int): Direction to move. 1 is down, -1 is up, 0 is same index.

        Returns:
            int: 1 if all words in target is accounted for.
        """
        if not self._validate_boundaries(r, c, row_dir, col_dir):
            return 0

        chain = 1
        for i in range(1, self.target_len):
            next_row = r + (row_dir * i)
            next_col = c + (col_dir * i)
            if (
                chain < self.target_len
                and self.puzzle[next_row][next_col] == self.target[i]
            ):
                chain += 1
            else:
                break

        return self._return_valid_count(chain)

    def _return_valid_count(self, chain):
        return 1 if chain == self.target_len else 0

    def search_right(self, r: int, c: int) -> int:
        """Search right for XMAS."""
        return self._search_direction(r, c, Dir.ZERO, Dir.RIGHT)

    def search_left(self, r: int, c: int) -> bool:
        """Search left for SMA'X'."""
        return self._search_direction(r, c, Dir.ZERO, Dir.LEFT)

    def search_down(self, r: int, c: int) -> bool:
        """Search down for
        X
        M
        A
        S.
        """
        return self._search_direction(r, c, Dir.DOWN, Dir.ZERO)

    def search_up(self, r: int, c: int) -> bool:
        """Search down for
        S
        A
        M
        X.
        """
        return self._search_direction(r, c, Dir.UP, Dir.ZERO)

    def search_diagonal_right_down(self, r: int, c: int) -> bool:
        """Search diagonal down for
        X...
        .M..
        ..A.
        ....S
        """
        return self._search_direction(r, c, Dir.DOWN, Dir.RIGHT)

    def search_diagonal_left_down(self, r: int, c: int) -> bool:
        """Search diagonal down for
        ...X
        ..M.
        .A..
        S...
        """
        return self._search_direction(r, c, Dir.DOWN, Dir.LEFT)

    def search_diagonal_right_up(self, r: int, c: int) -> bool:
        """Search diagonal up for
        ...S
        ..A.
        .M..
        X...
        """
        return self._search_direction(r, c, Dir.UP, Dir.RIGHT)

    def search_diagonal_left_up(self, r: int, c: int) -> bool:
        """Search diagonal left up for
        S...
        .A..
        ..M.
        ...X
        """
        return self._search_direction(r, c, Dir.UP, Dir.LEFT)


class XMasPuzzleFinder(PuzzleFinder):

    def __init__(self, puzzle, target):
        super().__init__(puzzle, target)
        self._validate_target_is_odd()
        self.mid_idx = self.target_len // 2
        self.mid_idx_coord = defaultdict(int)

    def _validate_target_is_odd(self):
        if self.target_len % 2 == 0:
            raise ValueError(f"{__class__} expects odd number length.")

    def _search_direction_with_memory(
        self,
        r: int,
        c: int,
        row_dir: int,
        col_dir: int,
    ) -> "XMasPuzzleFinder":
        """Search a specific direction in the n*n matrix, remembers the position of middle index.

        Args:
            r (int): Current row index.
            c (int): Current column index.
            row_dir (int): Direction to move. 1 is right, -1 is left, 0 is same index.
            col_dir (int): Direction to move. 1 is down, -1 is up, 0 is same index.

        Returns:
            int: 1 if all words in target is accounted for.
        """
        if not self._validate_boundaries(r, c, row_dir, col_dir):
            return 0

        chain = 1
        for i in range(1, self.target_len):
            next_row = r + (row_dir * i)
            next_col = c + (col_dir * i)
            if (
                chain < self.target_len
                and self.puzzle[next_row][next_col] == self.target[i]
            ):
                chain += 1
            else:
                break

        if self._return_valid_count(chain):
            mid_row = r + (row_dir * self.mid_idx)
            mid_col = c + (col_dir * self.mid_idx)
            self.mid_idx_coord[(mid_row, mid_col)] += 1

        return self

    def search_diagonal_right_down(self, r: int, c: int) -> "XMasPuzzleFinder":
        """
        Search diagonal right down for with memory of the middle coordinate.
        M..
        .A.
        ..S
        """
        return self._search_direction_with_memory(r, c, Dir.DOWN, Dir.RIGHT)

    def search_diagonal_left_down(self, r: int, c: int) -> "XMasPuzzleFinder":
        """
        Search diagonal left down for with memory of the middle coordinate.
        ..M
        .A.
        S..
        """
        return self._search_direction_with_memory(r, c, Dir.DOWN, Dir.LEFT)

    def search_diagonal_right_up(self, r: int, c: int) -> "XMasPuzzleFinder":
        """
        Search diagonal right up for with memory of the middle coordinate.
        ..S
        .A.
        M..
        """
        return self._search_direction_with_memory(r, c, Dir.UP, Dir.RIGHT)

    def search_diagonal_left_up(self, r: int, c: int) -> "XMasPuzzleFinder":
        """
        Search diagonal left up for with memory of the middle coordinate.
        S..
        .A.
        ..M
        """
        return self._search_direction_with_memory(r, c, Dir.UP, Dir.LEFT)


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
