"""Solution for day 1 2024."""

# Part 1
with open("data/input_1.txt", "r") as f:
    pair = [line.strip().split("   ") for line in f]


left = [int(p[0]) for p in pair]
right = [int(p[1]) for p in pair]

ans = 0
for l, r in zip(sorted(left), sorted(right)):
    ans += abs(l - r)

print(ans)

# Part 2
similarity_score = 0
for l in left:
    similarity_score += right.count(l) * l

print(similarity_score)
