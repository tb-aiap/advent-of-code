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

### Day 5

Stuggled a few days with this one trying to understand interval overlapping.

- **Part 1**: user regex to parse the seed value. Use a hash map to parse mappings for each level from level 1 to level 7.
    - for each seed, run through the mapping from level 1 to level 7
- **Part 2**: convert each seeds array into interval.
    1. Focus on passing a single array to the next level and remember the next level.
    2. If a seed range is not overlap in the mapping, try to match it again in the `for map in mapping` loop. Only pass it to the next level unmapped if cannot find any mapping ALL of the same level.

### Day 6

- **Part 1**: for each race, search through all combinations 1 by 1, increasing holding time.
- **Part 2**: Either use the same method, or use binary search. 
    1. Treat the input as one long race
    2. Binary search towards the left to find shortest time holding button to win race, any shorter is too slow
    3. Binary search towards the right to find the longest time holding button to win race, but any longer, not enough time to clear.

### Day 7

Create hashmap of suites and card value to assign as number
- **Part 1**: in order to sort the card by their values, assign a 2 digit value according to the order of their comparison. 
    - suite = value * 10000000000
    - card1 = value * 100000000
    - card2 = value * 1000000
    - card3 = value * 10000
    - card4 = value * 100
    - card5 = value * 1
- **Part 2**: Same steps as above with modification.
    - If `J` present in card, Try to get best_suite by replacing all possible combinations.
    - If `J` reassign to value 0, below `2` which is 1.

### Day 8 : Haunted Wasteland

Use iterator to cycle through the camel's instruction infinitely.

Convert the maps into a hashmap for indexing L and R location

- **Part 1**: Loop through the instructions from `AAA` till `ZZZ`
- **Part 2**: Each starting point `**A` hits their own respective `**Z` in a cycle. But each cycle is different, so LCM to find the time all of them hits it together. 

### Day 9: Mirage Maintenance

- **Part 1**: From top of the list, get the array difference and sum up the last index of the array
- **Part 2**: To get the front of the iteration, work from the bottom using the same formula.

### Day 10: Pipe Maze

- **Part 1**: A dirty method to try and follow the pipe logic from "S" starting point back to same starting point. It returns an `array` of coordinates. 
- **Part 2**: Struggled a few days to test own methods and various style. Settled with Reddit's most mentioned method of Pick's formula and Shoelace formula. 
    - Testing but hard to make it work.
    - BFS flooding from outer area, but there are smaller gaps that cannot be reached by BFS but it is not an interior
    - Ray casting to calcualte even and odd points, something wrong with my methodology to get it correct.

### Day 11: Cosmic Expansion 

- **Part 1**: 
    - Preprocess the empty rows/cols with a [0, 1]  array list.
    - For the distance between each galaxy, calculate manhattan distance
    - Slice the empty row array list for sum of 1s within that list
    - multiply it by expansion rate of 2
- **Part 2**: 
    - set expansion rate to 1,000,000


### Day 12: Hot Springs

Used ChatGpt to understand the optimal solution.

- **Part 1 & 2** : Walk through each idx of the springs, replacing '?' with both '.' and '#'. Upon placing a `.`, if `#` is there, try to complete the grouping else reject it. Use a memo dictionary to store previously accessed indexes.

### Day 13: Point of Incidence 

- **Part 1**: 
    - For each row, compare 2 adjacent row. If they are similar, initiate `while` loop to check reflection (l - 1 and r + 1) still remains the same.
    - If the loops break, it is not a valid reflection. (some portion on both ends are not part of the reflection)
    - If the loops end, we have a reflect from index `i`
- **Part 2**: 
    - same as above, but added a `smudge` param. 
    - instead of changing `.` to `#`. They are interchangeable. As long as there are 1 difference in smudge, we can reflect.
    - In order to advance the reflection check, either `l` and `r` idx must be the same, or have 1 smudge difference.
    - When the loop ends, check that we have advance till the end with only 1 smudge difference.

After checking other solution, another neater way is compare the mirror as a whole. By slicing the mirror and reversing the `after`, a `zip(before, after)` should be the same list if it reflects.
```python

grid_before = grid[:r]
grid_after = grid[r:][::1]

for l, r in zip(grid_before, grid_after):
    for a, b in zip(l, r):
        # compare each row element a and b
        ...
```
### Day 14: Parabolic Reflector Dish

- **Part 1**: 
    - Simulate a board tilt westward, using `loop` from left to right to count location of rocks.
    - Not ideal but, For every north, east, south tilt, massage/rotate it to fit a `westward_tilt` position.

- **Part 2**: 
    - Create a cycle by running the board into 4 tiles.
    - After 1 cycle, record the steps and board position in a hashmap. `first_seen`
    - Find out, how many more cycles until the board is seen in the same position as above as `second_seen`
    - Using this information, we can cut short 1 billion cycles by finding the remainder (after fast forwarding the same cycles.) 

### Day 15: Lens Library

- **Part 1**:
    - Just follow the instructions

- **Part 2**:
    - Create simulate the instruction with a list of array as the boxes and loop through each boxes based on the lens type.

### Day 16: The Floor Will Be Lava


- **Part 1**:
    - Simulate the laser shooting path one block at a time. Because the laser is splitted upon hitting `|` or `-`, there will be 2 different paths. So handing one each laser path one step at a time via a stack.

- **Part 2**:
    - For the maximum pew, simulate shooting a laser from all four corners of the grid.

### Day 17: Clumsy Crucible

- **Part 1 and 2**:
    - BFS to search through the lava map for all possible path to the destination.
    - Setting the restriction of BFS search to a specific min and max steps. So that the next step is invalid if it does not meet the rule required. 