# 2025 Solutions

### Day 1 : Secret Entrance
Tricky turns of a safe vault.
- **Part 1**: Simulate the safe dial turning using `% 100` to cycle through 99 to 1. There are also large turns `R435`, since each l00s are looping to the same spot, a floor div removes the loop.
- **Part 2**: to count for loops passing through 0, handle it via `floor div`.

### Day 2 : Gift Shop
`str` to `int` to `str` etc..
- **Part 1**: Only focus on even digit number, e.g. 1234. Then try to match 1212, upwards 1313, 1414 ... 9999 as long as it is within range
- **Part 2**: Same logic but start from 1 digit and increase it till the pair overshot.
    - 1234 -> 1 to 1111, 2 to 2222
    - 1234 -> 12 to 1212, 13 to 1313, 14 to 1414 etc
    - 1234 -> 123 to 123123 (cannot continue)

### Day 3 : Lobby 

Be greedy

- **Part 1:** Brute force the 2 digits. 

- **Part 2:** Build the largest possible 12-digit number by choosing digits in order from the string (a greedy subsequence). 
    - Always choose the highest possible digit (9 → 1) that still leaves enough characters to complete 12 digits. 
    - Repeat until the 12-digit sequence is formed, then sum across all lines.

### Day 4 : Printing Department 

Clear unstable asteroid blocks.

- **Part 1:** Count all @ blocks that have fewer than 4 adjacent @ neighbors (8-directional). No removal — just count once.

- **Part 2:** Repeatedly remove all @ blocks with <4 neighbors, update the grid, and continue until no more blocks can be removed. Count all removed blocks across all rounds.

### Day 5 : Cafeteria

Fresh or expired ingredients — verify ranges and merge them smartly.

- **Part 1:** Count how many ingredient numbers fall within any of the fresh-range intervals. Use a set to avoid double-counting ingredients that fall in multiple ranges.

- **Part 2:** Merge all overlapping or touching fresh-ranges, then count the total number of distinct values covered.
  - Sort intervals by their start.
  - Merge intervals when they overlap ([a,b] with [c,d]) by replacing the last merged interval with (a, max(b,d)).
  - This gives the total number of integers that are “fresh” across all combined ranges.

### Day 6 : Trash Compactor

`utils.py` messed me up with `[r.strip() for r in file]`. :w

- **Part 1:** Each column of numbers is a “question bank.” 
  - For each column, apply the operator (+ or *) from the last row to all numbers in that column.
  - Sum the results of all columns to get the final answer.

Key trick: collect numbers by column first, then reduce using the operator.

- **Part 2:** If the columns are padded properly, it is possble to `zip(*rows)` to read the lines vertically