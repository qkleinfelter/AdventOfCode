def day2p1(noun, verb):
    data = [int(x) for x in open(r'C:\Users\quinn.kleinfelter\Documents\AoC\Inputs\day2.txt').read().split(",")]
    data[1] = noun
    data[2] = verb
    currpos = 0
    while True:
        opcode = data[currpos]
        operand1 = data[currpos + 1]
        operand2 = data[currpos + 2]
        operand3 = data[currpos + 3]
        if(opcode == 99):
            break
        elif(opcode == 1):
            data[operand3] = data[operand1] + data[operand2]
        elif(opcode == 2):
            data[operand3] = data[operand1] * data[operand2]
        else:
            print("issue")
        currpos += 4
    return data[0]

def day2p2():
    for noun in range(100):
        for verb in range(100):
            if day2p1(noun, verb) == 19690720:
                return str(100 * noun + verb)

print(day2p1(12, 2))
print(day2p2())
