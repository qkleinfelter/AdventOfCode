def day6():
    data = open(r'Inputs\day6.in').read().split('\n\n')
    print('Part 1 result: ' + str(part1(data)))
    print('Part 2 result: ' + str(part2(data)))

def part1(data):
    totalq = 0
    for group in data:
        questions = set()
        people = group.split('\n')
        for person in people:
            for letter in person:
                questions.add(letter)
        totalq += len(questions)
    return totalq

def part2(data):
    totaleveryone = 0
    for group in data:
        questions = {}
        people = group.split('\n')
        for person in people:
            for letter in person:
                if letter in questions:
                    questions[letter] += 1
                else:
                    questions[letter] = 1
        for letter in questions:
            if questions[letter] == len(people):
                totaleveryone += 1
    return totaleveryone

day6()
