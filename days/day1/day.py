def main(day_input):
    dial = 50
    d_domain = 100
    psw_1, psw_2 = 0, 0
    for row in day_input:
        d,n = row[0], row[1:]
        s = -1 if d == 'L' else 1       
        
        for _ in range(int(n)):
            dial += s
            if dial == -1: dial = d_domain-1
            if dial == d_domain: dial = 0
            if dial == 0: psw_2 += 1
        
        if dial == 0: psw_1 += 1

    return psw_1, psw_2

