def day1():
    data = [int(x) for x in open(r'Inputs\day1.in')]
    print('Part 1 result: ' + str(part1(data)))
    print('Part 2 result: ' + str(part2(data)))

def part1(data):
    for x in data:
        # if 2020-x is in the data then those 2 numbers add to 2020 so multiply them and return
        if (2020 - x in data):
            return ((2020 - x) * x) 

def part2(data):
    for x in data:
        for y in data:
            for z in data:
                # if x y and z add to 2020 multiply and return
                if (x + y + z == 2020):
                    return (x*y*z)

day1()