import time
from collections import deque

def solution():
    data = open(r'2024\10\10.in').readlines()
    # data = open(r'2024\10\ex.in').readlines()
    data = [x.strip() for x in data]
    start = time.time()
    print('Part 1 result: ' + str(part1(data)))
    print(f'Finished p1 in {time.time() - start} seconds')
    start = time.time()
    print('Part 2 result: ' + str(part2(data)))
    print(f'Finished p2 in {time.time() - start} seconds')
    
#    right, left,   down,   up
D = [(0,1), (0,-1), (1,0), (-1,0)]
# simple bfs starting at a given position
def walk_trail_1(grid, r, c):
    R = len(grid)
    C = len(grid[0])
    visited = set()
    queue = deque()
    visited.add((r,c))
    queue.append((r,c))
    
    # we want distinct end positions for part 1 - i accidentally did this wrong first
    # and got the count of all paths which ended up being part 2
    ends = set()
    
    while queue:
        next = queue.popleft()
        visited.add(next)
        if grid[next[0]][next[1]] == 9:
            ends.add((next[0], next[1]))
        
        for dr, dc in D:
            newr, newc = next[0] + dr, next[1] + dc
            if 0 <= newr < R and 0 <= newc < C:
                # if moving in this direction is in the grid, we havent been there before,
                # and its the next number we care about, add it to the queue
                if grid[newr][newc] == grid[next[0]][next[1]] + 1 and (newr, newc) not in visited:
                    queue.append((newr, newc))
    
    return len(ends)

def part1(data):
    grid = [[int(c) for c in line] for line in data]
    R = len(grid)
    C = len(grid[0])
    trail_scores = 0
    for r in range(R):
        for c in range(C):
            if grid[r][c] == 0:
                score = walk_trail_1(grid, r, c)
                trail_scores += score
    return trail_scores

# this is the same as walk_trail_1 except we track ends via a counter rather than a set
# so we get all distinct hiking trails from each position, even if they end at the same
# location on the grid
def walk_trail_2(grid, r, c):
    R = len(grid)
    C = len(grid[0])
    visited = set()
    queue = deque()
    visited.add((r,c))
    queue.append((r,c))
    
    ends = 0
    
    while queue:
        next = queue.popleft()
        visited.add(next)
        if grid[next[0]][next[1]] == 9:
            ends += 1
        for dr, dc in D:
            newr, newc = next[0] + dr, next[1] + dc
            if 0 <= newr < R and 0 <= newc < C:
                if grid[newr][newc] == grid[next[0]][next[1]] + 1 and (newr, newc) not in visited:
                    queue.append((newr, newc))
    
    return ends


def part2(data):
    grid = [[int(c) for c in line] for line in data]
    R = len(grid)
    C = len(grid[0])
    trail_scores = 0
    for r in range(R):
        for c in range(C):
            if grid[r][c] == 0:
                score = walk_trail_2(grid, r, c)
                trail_scores += score
    return trail_scores

solution()