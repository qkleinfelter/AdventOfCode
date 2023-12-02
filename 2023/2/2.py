import math
import time


def solution():
    data = open(r'2023\2\2.in').readlines()
    # data = open(r'2023\2\ex.in').readlines()
    data = [x.strip() for x in data]
    start = time.time()
    print('Part 1 result: ' + str(part1(data)))
    print(f'Finished p1 in {time.time() - start} seconds')
    start = time.time()
    print('Part 2 result: ' + str(part2(data)))
    print(f'Finished p2 in {time.time() - start} seconds')
    
def part1(data):
    max_red, max_green, max_blue = 12, 13, 14
    sum_ids = 0
    for line in data:
        halves = line.split(":")
        game_id = halves[0].split(" ")[-1]
        groups = halves[1].split(";")
        higher_than_max = False
        for group in groups:
            colors = group.split(",")
            for color in colors:
                color = color.strip()
                split_color = color.split(" ")
                num = int(split_color[0])
                color_word = split_color[1]
                if color_word == 'red' and num > max_red:
                    higher_than_max = True
                elif color_word == 'green' and num > max_green:
                    higher_than_max = True
                elif color_word == 'blue' and num > max_blue:
                    higher_than_max = True
        if not higher_than_max:
            sum_ids += int(game_id)
    return sum_ids

def part2(data):
    sum_powers = 0
    for line in data:
        max_red, max_green, max_blue = -math.inf, -math.inf, -math.inf
        halves = line.split(":")
        game_id = halves[0].split(" ")[-1]
        groups = halves[1].split(";")
        for group in groups:
            colors = group.split(",")
            for color in colors:
                color = color.strip()
                split_color = color.split(" ")
                num = int(split_color[0])
                color_word = split_color[1]
                if color_word == 'red' and num > max_red:
                    max_red = num
                elif color_word == 'green' and num > max_green:
                    max_green = num
                elif color_word == 'blue' and num > max_blue:
                    max_blue = num
        sum_powers += (max_red * max_green * max_blue)
    return sum_powers

solution()