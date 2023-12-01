import itertools
from collections import defaultdict

data = open("C:/Users/Quinn/Documents/GitHub/AdventOfCode2018/src/Day4/day4input.txt").read().split("\n")
data.sort()

current_guard = 0
last_sleep = 0

for line in data:
    asleep = False
    if "Guard" in line:
        current_guard = line.split()[3].split("#")[1]
        asleep = False
    elif "falls asleep" in line:
        asleep = True
        last_sleep = line.split()[1]
    elif "wakes up" in line:
        asleep = False


