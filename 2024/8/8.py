import time
from collections import defaultdict
import itertools

def solution():
    data = open(r'2024\8\8.in').readlines()
    # data = open(r'2024\8\ex.in').readlines()
    data = [x.strip() for x in data]
    start = time.time()
    print('Part 1 result: ' + str(part1(data)))
    print(f'Finished p1 in {time.time() - start} seconds')
    start = time.time()
    print('Part 2 result: ' + str(part2(data)))
    print(f'Finished p2 in {time.time() - start} seconds')

p1_antinodes = set()

def p1_get_antinode(p1, p2, R, C):
    r1, c1 = p1
    r2, c2 = p2
    rdiff = r2 - r1
    cdiff = c2 - c1
    newr = r2 + rdiff
    newc = c2 + cdiff
    if 0 <= newr < R and 0 <= newc < C:
        p1_antinodes.add((newr, newc))
    
def part1(data):
    grid = [[c for c in line] for line in data]
    R = len(data)
    C = len(data[0])

    antennae = defaultdict(set)
    antinodes = set()
    for r in range(R):
        for c in range(C):
            item = grid[r][c]
            if item != ".":
                antennae[item].add((r,c))
    
    for antenna_type in antennae.keys():
        locs = list(antennae[antenna_type])
        pairs = itertools.combinations(locs, 2)
        for pair in pairs:
            n1, n2 = pair
            # this does the math to figure out the other antinodes associated with a pair
            # runs twice with the order reversed each time to make sure we get both directions
            p1_get_antinode(n1, n2, R, C)
            p1_get_antinode(n2, n1, R, C)

    return len(p1_antinodes)

p2_antinodes = set()

def p2_get_antinodes(p1, p2, R, C):
    r1, c1 = p1
    r2, c2 = p2
    rdiff = r2 - r1
    cdiff = c2 - c1
    newr = r2 + rdiff
    newc = c2 + cdiff

    # anytime we have a pair a tower is always an antinode so need to make sure this is in there
    p2_antinodes.add(p2)
    while 0 <= newr < R and 0 <= newc < C:
        p2_antinodes.add((newr, newc))
        newr += rdiff
        newc += cdiff

def part2(data):
    grid = [[c for c in line] for line in data]
    R = len(data)
    C = len(data[0])

    antennae = defaultdict(set)
    for r in range(R):
        for c in range(C):
            item = grid[r][c]
            if item != ".":
                antennae[item].add((r,c))
    
    for antenna_type in antennae.keys():
        locs = list(antennae[antenna_type])
        pairs = itertools.combinations(locs, 2)
        for pair in pairs:
            n1, n2 = pair
            # this does the math to figure out the other antinodes associated with a pair
            # runs twice with the order reversed each time to make sure we get both directions
            p2_get_antinodes(n1, n2, R, C)
            p2_get_antinodes(n2, n1, R, C)

    return len(p2_antinodes)

solution()