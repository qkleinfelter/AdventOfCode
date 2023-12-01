def day5():
    data = open(r'Inputs\day5.in').readlines()
    print('Part 1 result: ' + str(part1(data)))
    print('Part 2 result: ' + str(part2(data)))

def part1(data):
    # calculate the seatids for every seat in the data and return the maximum
    return max(calc_seat_id(line) for line in data)

def part2(data):
    # create a set of all the seatids
    seats = set(calc_seat_id(line) for line in data)
    # 127 rows = 127 * 8 ids
    for seatid in range(127 * 8):
        # if the seatid isn't in our list
        # and both +1 and -1 are in the list,
        # we've found our seat
        if seatid not in seats and seatid + 1 in seats and seatid - 1 in seats:
            return seatid
    
def calc_seat_id(line):
    # Binary counting, F and L are equivalent to 0 and B and R are equivalent to 1
    # this handles the row being multiplied by 8 since it is 3 spaces to the left in the binary number
    seatid = int(line.replace('F', '0').replace('L', '0').replace('B', '1').replace('R', '1'), 2)
    return seatid

day5()