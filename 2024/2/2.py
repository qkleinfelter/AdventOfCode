import itertools as it
import time


def solution():
    data = open(r'2024\2\2.in').readlines()
    # data = open(r'2024\2\ex.in').readlines()
    data = [x.strip() for x in data]
    start = time.time()
    print('Part 1 result: ' + str(part1(data)))
    print(f'Finished p1 in {time.time() - start} seconds')
    start = time.time()
    print('Part 2 result: ' + str(part2(data)))
    print(f'Finished p2 in {time.time() - start} seconds')
    
def part1(data):
    safe_count = 0

    for line in data:
        levels = line.split(' ')
        if is_safe(levels):
            safe_count += 1
    return safe_count

def part2(data):
    safe_count = 0

    for line in data:
        levels = line.split(' ')
        for i in range(len(levels)):
            new_list = levels[:i] + levels[i+1:]
            if is_safe(new_list):
                safe_count += 1
                break
    return safe_count

def is_safe(arr):
    row_diffs = []
    for i,j in it.pairwise(arr):
        difference = int(i)-int(j)
        row_diffs.append(difference)
    all_inc = all([True if x < 0 else False for x in row_diffs])
    all_dec = all([True if x > 0 else False for x in row_diffs])
    return (all_inc or all_dec) and all(1 <= abs(d) <= 3 for d in row_diffs)

solution()