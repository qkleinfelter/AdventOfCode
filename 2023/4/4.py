import time
from collections import defaultdict


def solution():
    data = open(r'2023\4\4.in').readlines()
    # data = open(r'2023\4\ex.in').readlines()
    data = [x.strip() for x in data]
    start = time.time()
    print('Part 1 result: ' + str(part1(data)))
    print(f'Finished p1 in {time.time() - start} seconds')
    start = time.time()
    print('Part 2 result: ' + str(part2(data)))
    print(f'Finished p2 in {time.time() - start} seconds')
    
def part1(data):
    pts = 0
    for line in data:
        winning, my_nums = line.split("|")
        winning = winning.split(":")[1].strip()
        winning_numbers = [int(num) for num in winning.split(" ") if num != '']
        my_numbers = [int(num) for num in my_nums.split(" ") if num != '']
        matches = -1
        for num in my_numbers:
            if num in winning_numbers:
                matches += 1
        if matches >= 0:
            pts += 2**matches
    return pts

def part2(data):
    card_wins = {}
    card_copies = defaultdict(lambda:1)
    for line in data:
        winning, my_nums = line.split("|")
        card_number, winning = winning.split(":")
        card_number = int(card_number.split(" ")[-1].strip())
        if card_copies.get(card_number) is None:
            card_copies[card_number] = 1
        winning = winning.strip()
        winning_numbers = [int(num) for num in winning.split(" ") if num != '']
        my_numbers = [int(num) for num in my_nums.split(" ") if num != '']
        if card_wins.get(card_number) is None:
            matches = 0
            for num in my_numbers:
                if num in winning_numbers:
                    matches += 1
            if matches >= 0:
                card_wins[card_number] = matches

        card_winnings = card_wins[card_number]
        copies_of_this_card = card_copies[card_number]
        for i in range(card_winnings):
            card_copies[card_number + i + 1] += 1 * copies_of_this_card
    total_cards = 0
    for value in card_copies.values():
        total_cards += value
    return total_cards
solution()