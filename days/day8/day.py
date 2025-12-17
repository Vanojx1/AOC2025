import math
from collections import defaultdict
from itertools import combinations
from operator import mul
from functools import reduce

def main(day_input):

    def d_3d(a, b):
        return math.sqrt(sum((xyz2-xyz1)**2 for xyz1, xyz2 in zip(a,b)))

    box_list = []
    for x, y, z in map(lambda r: map(int, r.split(',')), day_input):
        box_list.append((x, y, z))
    
    dist_map = {}
    circuits = {}
    for b1, b2 in combinations(box_list, 2):
        d = d_3d(b1, b2)
        dist_map[d] = (b1, b2)
        circuits[b1] = circuits[b2] = -1

    sorted_d = sorted(dist_map.keys())

    c_count = 0
    LIMIT = 1000
    for i, d in enumerate(sorted_d):

        b1, b2 = dist_map[d]

        if circuits[b1] == circuits[b2] == -1:
            circuits[b1] = circuits[b2] = c_count
            c_count += 1
        elif circuits[b1] == -1:
            circuits[b1] = circuits[b2]
        elif circuits[b2] == -1: 
            circuits[b2] = circuits[b1]
        elif circuits[b1] != circuits[b2]:
            circuits = {k: circuits[b1] if v == circuits[b2] else v for k, v in circuits.items()}

        if i == LIMIT:
            circ_counts = defaultdict(int)
            for v in circuits.values():
                if v == -1: continue
                circ_counts[v] += 1
            top_3 = reduce(mul, sorted(circ_counts.values(), reverse=True)[:3], 1)

        if len(set(circuits.values())) == 1:
            last_xx = b1[0] * b2[0]
            break

    return top_3, last_xx