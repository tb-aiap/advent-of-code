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