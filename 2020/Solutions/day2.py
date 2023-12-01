def day2():
    data = open(r'Inputs\day2.in').readlines()
    print('Part 1 result: ' + str(part1(data)))
    print('Part 2 result: ' + str(part2(data)))

def part1(data):
    valid = 0
    for x in data:
        # example line: 6-9 z: qzzzzxzzfzzzz
        # split each line on spaces, to get a set of numbers, a character to check and a password
        numbers, char, password = x.split()
        # split the numbers by the - and map them to ints as low and hi
        low, hi = map(int, numbers.split('-'))
        # remove the : in the char
        char = char[0]
        charct = 0
        for y in password:
            if y == char:
                # loop through the password looking for our char and increase the counter if we hit it
                charct += 1
        # if the number of chars is in our range increase the valid password counter
        if (low <= charct <= hi):
            valid += 1
    # return the number of valid passwords
    return valid

def part2(data):
    valid = 0
    for x in data:
        numbers, char, password = x.split()
        pos1, pos2 = map(int, numbers.split('-'))
        char = char[0]
        # same parsing as before
        # now check if the given positions (-1 since 1 indexed instead of 0) are our char
        # xor to handle only 1 of them being correct for validity
        if ((password[pos1-1] == char) ^ (password[pos2-1] == char)):
            valid += 1
    # return the number of valid passwords
    return valid
day2()