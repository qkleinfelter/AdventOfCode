import time
from collections import defaultdict


def solution():
    data = open(r'2023\3\3.in').readlines()
    # data = open(r'2023\3\ex.in').readlines()
    data = [x.strip() for x in data]
    start = time.time()
    print('Part 1 result: ' + str(part1(data)))
    print(f'Finished p1 in {time.time() - start} seconds')
    start = time.time()
    print('Part 2 result: ' + str(part2(data)))
    print(f'Finished p2 in {time.time() - start} seconds')
    
def part1(data):
    sum = 0
    grid = [[c for c in line] for line in data]
    max_rows = len(grid)
    max_cols = len(grid[0])
    for r in range(max_rows):
        number = ''
        touching_part = False
        for c in range(max_cols + 1):
            if c < max_cols and grid[r][c].isdigit():
                number += str(grid[r][c])
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        if 0 <= r + dr < max_rows and 0 <= c + dc < max_cols:
                            adj_char = grid[r+dr][c+dc]
                            if not adj_char.isdigit() and adj_char != '.':
                                touching_part = True
            elif number != '':
                if touching_part:
                    sum += int(number)
                number = ''
                touching_part = False
    return sum

def part2(data):
    sum = 0
    grid = [[c for c in line] for line in data]
    max_rows = len(grid)
    max_cols = len(grid[0])
    numbers_touching_gears = defaultdict(list)
    for r in range(max_rows):
        gears = set()
        number = ''
        for c in range(max_cols + 1):
            if c < max_cols and grid[r][c].isdigit():
                number += str(grid[r][c])
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        if 0 <= r + dr < max_rows and 0 <= c + dc < max_cols:
                            adj_char = grid[r+dr][c+dc]

                            if adj_char == "*":
                                gears.add((r + dr, c + dc))
            elif number != '':
                for gear in gears:
                    numbers_touching_gears[gear].append(int(number))
                number = ''
                gears = set()
    
    for key, value in numbers_touching_gears.items():
        if len(value) == 2:
            sum += value[0] * value[1]
    return sum

solution()