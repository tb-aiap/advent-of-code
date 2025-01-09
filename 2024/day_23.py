"""Solution for Day 23 2024."""

from collections import defaultdict

from utils import get_data, timer


@timer
def main(data: list[str]):

    part_1 = 0
    part_2 = 0
    t_hashmap = defaultdict(set)
    all_computers = set()

    for s in data:
        l, r = s.split("-")
        t_hashmap[l].add(r)
        t_hashmap[r].add(l)
        all_computers.update({r, l})

    t_set = set()
    for k in t_hashmap:
        if k.startswith("t"):
            for v in t_hashmap[k]:
                for w in t_hashmap[v]:
                    if w in t_hashmap[k]:
                        t_set.add(tuple(sorted([k, v, w])))

    # PART 2
    part_2 = defaultdict(set)
    part_2a = defaultdict(int)
    for k in t_hashmap:
        for l in t_hashmap[k]:
            part_2[k].update(t_hashmap[k].intersection(t_hashmap[l]))
            part_2[k].add(k)

    result = 0
    for k in part_2:
        lan_party = tuple(sorted(list(part_2[k])))
        part_2a[lan_party] += 1
        if result < part_2a[lan_party]:
            lan_set = lan_party
            result = part_2a[lan_party]

    part_1 = len(t_set)
    part_2 = ",".join(lan_set)

    return part_1, part_2


if __name__ == "__main__":

    data = get_data(23)
    part_1, part_2 = main(data)

    print("Solution for Part 1", part_1)
    print("Solution for Part 2", part_2)
