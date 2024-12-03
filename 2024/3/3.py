import time
import re

def solution():
    data = open(r'2024\3\3.in').read()
    # data = open(r'2024\3\ex.in').read()
    start = time.time()
    print('Part 1 result: ' + str(part1(data)))
    print(f'Finished p1 in {time.time() - start} seconds')
    start = time.time()
    print('Part 2 result: ' + str(part2(data)))
    print(f'Finished p2 in {time.time() - start} seconds')
    
mul_regex = 'mul\((\d{1,3}),(\d{1,3})\)'
# I started out trying to do some weird stuff with this before 
# I realized I could put all of them in one pattern and just loop through it lol
# do_regex = 'do\(\)'
# dont_regex = "don\'t\(\)"

def part1(data):
    pairs = re.findall(mul_regex, data)
    sum = 0
    for pair in pairs:
        sum += int(pair[0]) * int(pair[1])
    return sum

# capturing groups messed up my do/don't so I'm just using it regularly here
p2_regex = "mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)"
def part2(data):
    matches = re.findall(p2_regex, data)
    sum = 0
    currently_doing = True
    for match in matches:
        if match == "don't()":
            currently_doing = False
        elif match == "do()":
            currently_doing = True
        else:
            if currently_doing:
                # i already know this will match because of the first regex, this findall is purely
                # to let regex use capturing groups to help me out
                pair = re.findall(mul_regex, match)[0]
                sum += int(pair[0]) * int(pair[1])
        
    return sum

solution()
