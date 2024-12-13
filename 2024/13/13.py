import time
import re

def solution():
    data = open(r'2024\13\13.in').read().split('\n\n')
    # data = open(r'2024\13\ex.in').read().split('\n\n')
    data = [x.strip() for x in data]
    start = time.time()
    print('Part 1 result: ' + str(part1(data)))
    print(f'Finished p1 in {time.time() - start} seconds')
    start = time.time()
    print('Part 2 result: ' + str(part2(data)))
    print(f'Finished p2 in {time.time() - start} seconds')
    
x_y_reg = r'X\+(\d+), Y\+(\d+)'
prize_reg = r'X=(\d+), Y=(\d+)'
def part1(data):
    total_tokens_needed = 0
    for problem in data:
        a, b, prize = problem.split('\n')
        a_x, a_y = re.findall(x_y_reg, a)[0]
        b_x, b_y = re.findall(x_y_reg, b)[0]
        prize_x, prize_y = re.findall(prize_reg, prize)[0]
        total_tokens_needed += solve_system(int(a_x), int(a_y), int(b_x), int(b_y), int(prize_x), int(prize_y))
    return total_tokens_needed

# system of 2 equations with 2 unknowns
def solve_system(a_x, a_y, b_x, b_y, prize_x, prize_y) -> int:
    denom = (a_x * b_y) - (a_y * b_x)
    a_num = (prize_x * b_y) - (prize_y * b_x)
    b_num = (a_x * prize_y) - (a_y * prize_x)
    a = a_num // denom
    b = b_num // denom
    eq_soln = (a_x * a + b_x * b, a_y * a + b_y * b)
    if eq_soln == (prize_x, prize_y):
        return 3 * a + 1 * b
    return 0

def part2(data):
    total_tokens_needed = 0
    for problem in data:
        a, b, prize = problem.split('\n')
        a_x, a_y = re.findall(x_y_reg, a)[0]
        b_x, b_y = re.findall(x_y_reg, b)[0]
        prize_x, prize_y = re.findall(prize_reg, prize)[0]
        total_tokens_needed += solve_system(int(a_x), int(a_y), int(b_x), int(b_y), int(prize_x) + 10000000000000, int(prize_y) + 10000000000000)
    return total_tokens_needed

solution()