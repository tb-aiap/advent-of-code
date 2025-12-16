"""Solution for Day 8 2025."""

import math

import utils

xyz = tuple[int, int, int]

NUM_OF_CIRCUIT = 1000


def get_euclidean_distance(p1: xyz, p2: xyz):
    return math.dist(p1, p2)


def solve(data, part2=False):
    circuits: list[xyz] = []
    for box in data:
        x, y, z = map(int, box.split(","))
        circuits.append((x, y, z))

    n = len(circuits)
    all_edges_idx: list[tuple[float, int, int]] = []
    for i in range(n):
        for j in range(i + 1, n):
            dist = get_euclidean_distance(circuits[i], circuits[j])
            all_edges_idx.append((dist, i, j))

    all_edges_idx = sorted(all_edges_idx, key=lambda x: x[0])

    parent = list(range(n))
    # size = [1] * n

    def find(x: int) -> int:
        if parent[x] != x:
            parent[x] = find(parent[x])

        return parent[x]

    def union(a: int, b: int):
        ra, rb = find(a), find(b)
        if ra == rb:
            return False

        parent[rb] = ra
        # size[ra] += size[rb]
        return True

    attempt = 0
    last_edge = None
    for _, i, j in all_edges_idx:
        merged = union(i, j)
        attempt += 1

        if merged:
            last_edge = (i, j)

        if not part2 and attempt == NUM_OF_CIRCUIT:
            break

    if part2:
        x1, x2 = circuits[last_edge[0]][0], circuits[last_edge[1]][0]
        return x1 * x2

    # part 1
    circuits_size: dict[int, int] = {}
    for i in range(n):
        root = find(i)
        circuits_size[root] = circuits_size.get(root, 0) + 1

    sizes = sorted(circuits_size.values(), reverse=True)
    part_1 = sizes[0] * sizes[1] * sizes[2]
    return part_1


@utils.timer
def main(data):
    part_1 = solve(data)
    part_2 = solve(data, True)

    return part_1, part_2
