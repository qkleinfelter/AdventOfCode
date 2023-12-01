import itertools

data = [int(x) for x in open("C:/Users/Quinn/Documents/GitHub/AdventOfCode2018/src/Day1/day1input.txt")]

print(sum(data))

freq = 0
seen = {0}
for num in itertools.cycle(data):
    freq += num
    if freq in seen:
        print(freq)
        break
    seen.add(freq)