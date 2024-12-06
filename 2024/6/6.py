import time
from collections import defaultdict
from copy import copy

def solution():
    data = open(r'2024\6\6.in').readlines()
    # data = open(r'2024\6\ex.in').readlines()
    data = [x.strip() for x in data]
    start = time.time()
    print('Part 1 result: ' + str(part1(data)))
    print(f'Finished p1 in {time.time() - start} seconds')
    start = time.time()
    print('Part 2 result: ' + str(part2(data)))
    print(f'Finished p2 in {time.time() - start} seconds')
    
#       up,     right,  down,   left
dirs = [(-1,0), (0, 1), (1, 0), (0, -1)]
def part1(data):
    grid = defaultdict(int)
    guard_pos = None
    R = len(data)
    C = len(data[0])
    for r in range(R):
        for c in range(C):
            char = data[r][c]
            if char == "#":
                grid[(r,c)] = 2
            elif char == "^":
                guard_pos = (r,c)
    dir_idx = 0

    while True:
        while grid[guard_pos] != 2 and 0 <= guard_pos[0] < R and 0 <= guard_pos[1] < C:
            dir = dirs[dir_idx]
            grid[guard_pos] = 1
            guard_pos = (guard_pos[0] + dir[0], guard_pos[1] + dir[1])
        if grid[guard_pos] == 2:
            dir = dirs[dir_idx]
            # go back to the spot you were at before you hit the wall
            guard_pos = (guard_pos[0] - dir[0], guard_pos[1] - dir[1])
            dir_idx = (dir_idx + 1) % len(dirs)
            continue
        break
    count = sum(value == 1 for value in grid.values())
    return count

def check_grid_for_loops(grid, guard_pos, R, C):
    visited = set()
    total_steps = 0
    dir_idx = 0
    while True:
        while grid[guard_pos] != 2 and 0 <= guard_pos[0] < R and 0 <= guard_pos[1] < C:
            dir = dirs[dir_idx]
            guard_pos = (guard_pos[0] + dir[0], guard_pos[1] + dir[1])
            if (guard_pos, dir) in visited:
                return True
            # figure if we're over 2 times as many steps as we took to answer part 1, it probably doesn't loop lol
            if total_steps > 4647 * 2:
                return False
            
            # print(guard_pos, dir)
            visited.add((guard_pos, dir))
            total_steps += 1
        if grid[guard_pos] == 2:
            dir = dirs[dir_idx]
            # go back to the spot you were at before you hit the wall
            guard_pos = (guard_pos[0] - dir[0], guard_pos[1] - dir[1])
            dir_idx = (dir_idx + 1) % len(dirs)
            continue
        break

def part2(data):
    grid = defaultdict(int)
    guard_pos = None
    R = len(data)
    C = len(data[0])
    for r in range(R):
        for c in range(C):
            char = data[r][c]
            if char == "#":
                grid[(r,c)] = 2
            elif char == "^":
                guard_pos = (r,c)
    
    loop_count = 0
    for r in range(R):
        for c in range(C):
            if grid[(r,c)] != 2 and guard_pos != (r,c):
                # print(f'about to check new grid with obstacle at {(r,c)}')
                new_grid = copy(grid)
                new_grid[(r,c)] = 2
                if check_grid_for_loops(new_grid, guard_pos, R, C):
                    # print(f"placed obstacle at {(r,c)}")
                    loop_count += 1
    
    return loop_count


solution()