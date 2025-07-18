# 2023 solutions

### Day 1
Sliding through each character to identify number or words. Coverting them into digit string, then getting the first and last digit.

#### Part 2
`twoneighthree` is an edge case

### Day 2
Constant splitting of text to gather the required input text.

### Day 3
- **Part 1**: While scanning each row, build numbers digit by digit. For each digit, check all 8 surrounding cells. If any symbol (non-digit, non-dot) is adjacent to any digit in the number, add the full number to the sum.

- **Part 2**: Similar to Part 1, but checks for adjacent * characters (gears). If a number is adjacent to a gear, it is associated with that gear's coordinates. After scanning, only gears with exactly two adjacent numbers are used to compute gear ratios (product of the two numbers).
- Potential bug, part 2 assumes each number is tag to a single gear "*".

### Day 4

- **Part 1**: The total score, where each card's score is `2**(matches - 1)` if at least one number matches.

- **Part 2**: Maintain the function for part 1, but multiply results by number of copies it has. Add the number of copies into subsequent cards. 