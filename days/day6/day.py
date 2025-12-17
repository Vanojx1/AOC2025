import re
from functools import reduce

def main(day_input):
    *rows, ops = day_input
    spans = [m.span() for m in re.finditer(r'([*+]\s+)\s', ops)]
    ops = list(re.sub(r' ', '', ops))

    g_total_1, g_total_2 = 0, 0
    for i, (a, b) in enumerate(spans):
        nums_1 = [int(row[a:b]) for row in rows]
        nums_2 = [(''.join(rows[j][i] for j in range(len(rows)))).strip() for i in range(a, b)]
        op = ops[i]

        if op == '*':
            g_total_1 += reduce(lambda c,n: c*n, nums_1, 1)
            g_total_2 += reduce(lambda c,n: c*(int(n) if n != '' else 1), nums_2, 1)
        else:
            g_total_1 += reduce(lambda c,n: c+n, nums_1, 0)
            g_total_2 += reduce(lambda c,n: c+(int(n) if n != '' else 0), nums_2, 0)

    return g_total_1, g_total_2