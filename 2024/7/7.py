from operator import add, mul
import time


def solution():
    data = open(r'2024\7\7.in').readlines()
    # data = open(r'2024\7\ex.in').readlines()
    data = [x.strip() for x in data]
    start = time.time()
    print('Part 1 result: ' + str(part1(data)))
    print(f'Finished p1 in {time.time() - start} seconds')
    start = time.time()
    print('Part 2 result: ' + str(part2(data)))
    print(f'Finished p2 in {time.time() - start} seconds')

def concat(a, b):
    return int(f"{a}{b}")

p1_operators = [add, mul]
p2_operators = [add, mul, concat]
    
def part1(data):
    sum_of_valid_results = 0
    for row in data:
        split = row.split(": ")
        target = int(split[0])
        equation_numbers = [int(x) for x in split[1].split(" ")]
        
        sum_of_valid_results += solve([target, *equation_numbers], p1_operators)
    return sum_of_valid_results

# numbers should be the target value, followed by the list of numbers to evaluate
def solve(numbers, operators):
    # if we only have 2 numbers, that means we evaluated all of them
    # and we should just compare the target to the value we evaluated against in this tree
    if len(numbers) == 2:
        return numbers[0] == numbers[1]
    
    # destructure numbers into some things we can use appropriately
    target, a, b, *rest = numbers
    # start a recursive chain for each of the operators with the next 2 numbers
    for op in operators:
        # if we get a number that is not 0 back we should return the target value because its a valid chain
        if solve([target, op(a, b)] + rest, operators) != 0:
            return target

    # if we make it here that means none of the chains downstream of here work, so return 0
    return 0

def part2(data):
    sum_of_valid_results = 0
    for row in data:
        split = row.split(": ")
        target = int(split[0])
        equation_numbers = [int(x) for x in split[1].split(" ")]
        
        sum_of_valid_results += solve([target, *equation_numbers], p2_operators)
    return sum_of_valid_results

solution()