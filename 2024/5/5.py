import time
from collections import defaultdict

def solution():
    data = open(r'2024\5\5.in').read().split('\n\n')
    # data = open(r'2024\5\ex.in').read().split('\n\n')
    data = [x.strip() for x in data]
    start = time.time()
    print('Part 1 result: ' + str(part1(data)))
    print(f'Finished p1 in {time.time() - start} seconds')
    start = time.time()
    print('Part 2 result: ' + str(part2(data)))
    print(f'Finished p2 in {time.time() - start} seconds')
    
def part1(data):
    rules = data[0].split()
    updates = data[1].split()
    rules_d = defaultdict(set)
    for rule in rules:
        spl = [int(x) for x in rule.split('|')]
        rules_d[spl[0]].add(spl[1])
    
    correct_ordered_updates = []
    for update in updates:
        update = [int(x) for x in update.split(',')]
        seen_pages = set()
        bad_update = False
        for page in update:
            following_pages = rules_d[page]
            intersect = seen_pages.intersection(following_pages)
            if len(intersect) != 0:
                bad_update = True
            seen_pages.add(page)
        if not bad_update:
            correct_ordered_updates.append(update)

    sum = 0
    for update in correct_ordered_updates:
        sum += update[(len(update) - 1)//2]
    return sum

def part2(data):
    rules = data[0].split()
    updates = data[1].split()
    rules_d = defaultdict(set)
    for rule in rules:
        spl = [int(x) for x in rule.split('|')]
        rules_d[spl[0]].add(spl[1])
    
    incorrect_ordered_updates = []
    for update in updates:
        update = [int(x) for x in update.split(',')]
        seen_pages = set()
        bad_update = False
        for page in update:
            following_pages = rules_d[page]
            intersect = seen_pages.intersection(following_pages)
            if len(intersect) != 0:
                bad_update = True
            seen_pages.add(page)
        if bad_update:
            incorrect_ordered_updates.append(update)

    reordered_updates = []
    for update in incorrect_ordered_updates:
        seen_pages = set()
        i = 0
        # originally tried using range here but figured out that I was missing some moves so switched to this
        while i < len(update):
            page = update[i]
            following_pages = rules_d[page]
            intersect = seen_pages.intersection(following_pages)
            if len(intersect) != 0:
                # take wherever the intersection was before, and put it after the current page
                for to_move in intersect:
                    update_idx = update.index(to_move)
                    update.insert(i, update.pop(update_idx))
                    seen_pages.remove(to_move)
                    i -= 1
            seen_pages.add(page)
            i += 1
        reordered_updates.append(update)

    sum = 0
    for update in reordered_updates:
        sum += update[(len(update) - 1)//2]
    return sum

solution()