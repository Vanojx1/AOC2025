def main(day_input):
    papers = {complex(x, y) for y, row in enumerate(day_input) for x, v in enumerate(row) if v == '@'}
    offs = (1+0j, 1+1j, 1j, -1+1j, -1+0j, -1-1j, -1j, 1-1j)

    total_1, total_2 = 0, 0
    while True:
        to_remove = set([])
        for paper in papers:
            if len([() for off in offs if paper+off in papers]) < 4:
                to_remove.add(paper)

        if not total_1: total_1 = len(to_remove)
        total_2 += len(to_remove)
        papers -= to_remove
        if not to_remove: break

    return total_1, total_2