# 2025 Solutions

### Day 1 : Secret Entrance
Tricky turns of a safe vault.
- **Part 1**: Simulate the safe dial turning using `% 100` to cycle through 99 to 1. There are also large turns `R435`, since each l00s are looping to the same spot, a floor div removes the loop.
- **Part 2**: to count for loops passing through 0, handle it via `floor div`.