import math
def day1():
    data = [int(x) for x in open(r'C:\Users\quinn.kleinfelter\Documents\AoC\Inputs\day1.txt')]
    sum = 0
    for x in data:
        sum = sum + getfuel(x)
    print(sum)

def getfuel(num):
    fuel = (math.floor(num / 3) - 2)
    if(fuel <= 0):
        return 0
    else:
        return fuel + getfuel(fuel)

day1()