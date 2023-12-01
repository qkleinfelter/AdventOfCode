import time


def solution():
    data = open(r'2023\1\1.in').readlines()
    # data = open(r'2023\1\ex.in').readlines()
    data = [x.strip() for x in data]
    start = time.time()
    # print('Part 1 result: ' + str(part1(data)))
    # print(f'Finished p1 in {time.time() - start} seconds')
    start = time.time()
    print('Part 2 result: ' + str(part2(data)))
    print(f'Finished p2 in {time.time() - start} seconds')
    
def part1(data):
    sum = 0
    for line in data:
        num = ''
        for char in line:
            if char in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
                num += char
        num = int(num[0] + num[-1])
        sum += num
    return sum

mapping = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}
def part2(data):
    sum = 0
    for line in data:
        num = ''
        for char in line:
            if char in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
                num += char
        num = int(num[0] + num[-1])
        sum += num
    return sum

solution()