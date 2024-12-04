import time


def solution():
    data = open(r'2024\4\4.in').readlines()
    # data = open(r'2024\4\ex.in').readlines()
    data = [x.strip() for x in data]
    start = time.time()
    print('Part 1 result: ' + str(part1(data)))
    print(f'Finished p1 in {time.time() - start} seconds')
    start = time.time()
    print('Part 2 result: ' + str(part2(data)))
    print(f'Finished p2 in {time.time() - start} seconds')

# movements we can make
directions = [(0,1),(1,0),(0,-1),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)]
target = ["X", "M", "A", "S"]

def check_adj_chars(ws, r, c):
    sum = 0
    for dr, dc in directions:
        found = False
        for i in range(3):
            inc = i + 1
            new_r = r+(dr*inc)
            new_c = c+(dc*inc)
            if 0 <= new_r <= len(ws) - 1 and 0 <= new_c <= len(ws[r]) - 1:
                next_char = ws[new_r][new_c]
                if next_char != target[inc]:
                    break
                if next_char == "S":
                    found=True
        if found:
            sum += 1
    return sum

def part1(data) -> int:
    ws = [[c for c in line] for line in data]
    chrimma_cnt = 0
    for r in range(len(ws)):
        for c in range(len(ws[r])):
            if ws[r][c] == "X":
                words = check_adj_chars(ws, r, c)
                chrimma_cnt += words
    return chrimma_cnt

other_checks = [((1,1), (-1, -1)), ((1, -1), (-1, 1))]
# true if we failed to find an x-mas, i know its backwards
def check_for_x_mas(ws, r, c):
    pair_failed = False
    for pair in other_checks:
        n1 = (r + pair[0][0], c + pair[0][1])
        n2 = (r + pair[1][0], c + pair[1][1])
        # make sure both other squares are valid
        if (0 <= n1[0] <= len(ws) - 1 and 0 <= n1[1] <= len(ws[r]) - 1) and (0 <= n2[0] <= len(ws) - 1 and 0 <= n2[1] <= len(ws[r]) - 1):
            c1 = ws[n1[0]][n1[1]]
            c2 = ws[n2[0]][n2[1]]
            if not ((c1 == "S" and c2 == "M") or (c1 == "M" and c2 == "S")):
                pair_failed = True
        else:
            pair_failed = True
    return pair_failed

def part2(data) -> int:
    ws = [[c for c in line] for line in data]
    x_mas_ct = 0
    for r in range(len(ws)):
        for c in range(len(ws[r])):
            # determine if we're in the middle of an X-MAS
            if ws[r][c] == "A":
                if not check_for_x_mas(ws, r, c):
                    x_mas_ct += 1
    return x_mas_ct

solution()