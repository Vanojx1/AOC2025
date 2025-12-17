from dataclasses import dataclass
import functools

def main(day_input):

    @dataclass
    class Node:
        leafs: set

    splitters = set()
    nodes = {}
    H = len(day_input)
    for y, row in enumerate(day_input):
        for x, v in enumerate(row):
            if v == 'S':
                start = (x, y)
            elif v == '^':
                splitters.add((x, y))
    
    beams = set([start])
    split = 0
    while True:
        new_beams = set()
        for x, y in beams:
            if (n_b := (x, y+1)) in splitters:
                new_beams.add((x-1, y+1))
                new_beams.add((x+1, y+1))
                split += 1
            else: 
                new_beams.add(n_b)
        beams = set(new_beams)
        if next(iter(beams))[1] == H-1: break

    @functools.cache
    def go_down(pos, parent=None):
        x, y = pos

        if pos not in nodes:
            nodes[pos] = Node(set())
        
        if parent is not None:
            nodes[parent].leafs.add(pos)
        
        for y1 in range(y+1, H):
            if (x, y1) in splitters:
                go_down((x-1, y1), pos)
                go_down((x+1, y1), pos)
                break
            if y1 == H-1: go_down((x, y1), pos)

    go_down(start)
    
    @functools.cache
    def traverse(pos):
        n = nodes[pos]
        if len(n.leafs) == 0: return 1
        return sum(traverse(l) for l in n.leafs)

    return split, traverse(start)