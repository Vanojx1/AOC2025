def main(day_input):
    ranges = [(a,b) for a,b in map(lambda x:x.split('-'), day_input[0].split(','))]

    total_1 = 0
    total_2 = 0
    for a, b in ranges:
        for n in range(int(a), int(b)+1):
            s_n = str(n)
            l = len(s_n)

            if l % 2 == 0 and s_n[:l//2] == s_n[l//2:]:
                total_1 += n

            for step in range(1, (l // 2) + 1):
                parts = [s_n[i:i+step] for i in range(0, len(s_n), step)]
                if l % step == 0 and all(parts[0] == part for part in parts):
                    total_2 += n
                    break

    return total_1, total_2