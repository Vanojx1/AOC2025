import re

def main(day_input):

    ranges = []
    ingredients = []
    for row in day_input:
        if m := re.match(r'(\d+)-(\d+)', row):
            ranges.append((int(m.group(1)), int(m.group(2))))
        elif m := re.match(r'(\d+)', row):
            ingredients.append(int(m.group(1)))
    
    ranges.sort(key=lambda x: x[0])
    opt_ranges = []
    for s, e in ranges:
        if not opt_ranges: opt_ranges.append([s, e])
        else:
            if s <= opt_ranges[-1][1]:
                if e > opt_ranges[-1][1]:
                    opt_ranges[-1][1] = e
            else:
                opt_ranges.append([s, e])

    in_range = 0
    for ing in ingredients:
        for a, b in opt_ranges:
            if a <= ing <= b:
                in_range += 1

    total_fresh = sum([b-a+1 for a, b in opt_ranges])

    return in_range, total_fresh