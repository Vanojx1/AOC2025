from collections import defaultdict

def main(day_input):
    total_1, total_2 = 0,0
    for bank in day_input:
        banks_map = defaultdict(list)
        for i, b in enumerate(bank):
            banks_map[int(b)].append(i)

        def get_max_joltage(size, curr=[]):
            if len(curr) == size: return int(''.join(str(bank[i]) for i in curr))
            for p1 in range(9, -1, -1):
                for i in banks_map[p1]:
                    if (not curr or i > curr[-1]) and (r := get_max_joltage(size, curr + [i])):
                        return r 
            return 0

        total_1 += get_max_joltage(2)
        total_2 += get_max_joltage(12)

    return total_1, total_2