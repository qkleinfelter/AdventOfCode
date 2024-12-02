import time
from collections import defaultdict


def solution():
    data = open(r'2024\1\1.in').readlines()
    # data = open(r'2024\1\ex.in').readlines()
    data = [x.strip() for x in data]
    start = time.time()
    print('Part 1 result: ' + str(part1(data)))
    print(f'Finished p1 in {time.time() - start} seconds')
    start = time.time()
    print('Part 2 result: ' + str(part2(data)))
    print(f'Finished p2 in {time.time() - start} seconds')
    
def part1(data):
    list1, list2 = [], []
    for line in data:
        (l1, l2) = line.split('   ')
        list1.append(int(l1))
        list2.append(int(l2))

    list1.sort()
    list2.sort()
    
    total_dist = 0
    for l,r in zip(list1, list2):
        dist = abs(l - r)
        total_dist += dist
    return total_dist

def part2(data):
    list1 = []
    list2_count = defaultdict(int)
    for line in data:
        (l1, l2) = line.split('   ')
        list1.append(int(l1))
        list2_count[int(l2)] += 1
    
    total_similarity = 0
    for num in list1:
        similarity = list2_count[num]
        total_similarity += num * similarity
    return total_similarity

solution()