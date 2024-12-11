import time
from collections import defaultdict

def solution():
    data = open(r'2024\11\11.in').read().split(' ')
    # data = open(r'2024\11\ex.in').read().split(' ')
    data = [x.strip() for x in data]
    start = time.time()
    print('Part 1 result: ' + str(part1(data)))
    print(f'Finished p1 in {time.time() - start} seconds')
    start = time.time()
    print('Part 2 result: ' + str(part2(data)))
    print(f'Finished p2 in {time.time() - start} seconds')
    
def part1(data):
    stones = [int(x) for x in data]
    stone_counts = defaultdict(int)
    for stone in stones:
        stone_counts[stone] += 1
    for _ in range(25):
        new_stone_counts = defaultdict(int)
        for stone, stone_count in stone_counts.items():
            if stone == 0 and stone_count > 0:
                new_stone_counts[1] += stone_count
            elif len(str(stone)) % 2 == 0 and stone_count > 0:
                str_stone = str(stone)
                left = int(str_stone[:len(str_stone) // 2])
                right = int(str_stone[len(str_stone) // 2:])
                new_stone_counts[left] += stone_count
                new_stone_counts[right] += stone_count
            else:
                if stone_count == 0:
                    continue
                new_stone_counts[stone * 2024] = stone_count
        stone_counts = new_stone_counts
    total_stones = sum(stone_counts.values())
    return total_stones

def part2(data):
    stones = [int(x) for x in data]
    stone_counts = defaultdict(int)
    for stone in stones:
        stone_counts[stone] += 1
    for _ in range(75):
        new_stone_counts = defaultdict(int)
        for stone, stone_count in stone_counts.items():
            if stone == 0 and stone_count > 0:
                new_stone_counts[1] += stone_count
            elif len(str(stone)) % 2 == 0 and stone_count > 0:
                str_stone = str(stone)
                left = int(str_stone[:len(str_stone) // 2])
                right = int(str_stone[len(str_stone) // 2:])
                new_stone_counts[left] += stone_count
                new_stone_counts[right] += stone_count
            else:
                if stone_count == 0:
                    continue
                new_stone_counts[stone * 2024] = stone_count
        stone_counts = new_stone_counts
    total_stones = sum(stone_counts.values())
    return total_stones

solution()