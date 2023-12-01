def day3():
    data = open(r'Inputs\day3.in').read().splitlines()
    print('Part 1 result: ' + str(part1(data, 3, 1)))
    print('Part 2 result: ' + str(part2(data)))

def part1(data, right, down):
    x = 0
    dx = right # change in x
    dy = down  # change in y
    trees = 0  # number of trees

    # loop through the rows, starting at 0 and increasing by the change in y each time
    for y in range(0, len(data), dy):
        # if our current spot is a # increment trees
        if (data[y][x] == "#"):
            trees += 1
        # increase x by the change in x value and then mod it with the length of the row
        # this handles the pattern looping
        x = (x + dx) % len(data[0])
    return trees

def part2(data):
    # each of these is one slope we want to try on the same algorithm
    slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
    total = 1
    # run part 1 with each of the slopes in the list
    # multiplying the results by each other
    for slope in slopes:
        total *= part1(data, slope[0], slope[1])
    return total

day3()