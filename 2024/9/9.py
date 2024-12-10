import time


def solution():
    # data = open(r'2024\9\9.in').read()
    data = open(r'2024\9\ex.in').read()
    start = time.time()
    print('Part 1 result: ' + str(part1(data)))
    print(f'Finished p1 in {time.time() - start} seconds')
    start = time.time()
    print('Part 2 result: ' + str(part2(data)))
    print(f'Finished p2 in {time.time() - start} seconds')

def swap_chars(str, i, j):
    arr = list(str)
    arr[i], arr[j] = arr[j], arr[i]
    return ''.join(arr)
    
def part1(data):
    expanded_str = ''
    is_free = False
    # find the ordinal code for 0 so we can start there
    # this allows us to chr(file_index) when building out the string later
    # so that we can avoid problems with indexes >9 being multiple characters
    # in the string
    file_index = ord('0')
    for c in data:
        if is_free:
            expanded_str += "."*int(c)
        else:
            expanded_str += chr(file_index)*int(c)
            file_index += 1
        is_free = not is_free
    print('Finished expanding string')

    reversed = expanded_str[::-1]
    ans_str = expanded_str[:]
    for i,c in enumerate(reversed):
        if c != ".":
            first_free = ans_str.index('.')
            ans_str = swap_chars(ans_str, len(reversed) - i - 1, first_free)
        check = ans_str.index('.')
        if check >= len(reversed) - i - 1:
            break
    print('Finished Swapping Characters')

    checksum = 0
    original_ord = ord('0')
    for i,c in enumerate(ans_str):
        if c == ".":
            continue
        file_id = ord(c) - original_ord
        checksum += i * file_id
    return checksum

def part2(data):
    expanded_str = ''
    is_free = False
    # find the ordinal code for 0 so we can start there
    # this allows us to chr(file_index) when building out the string later
    # so that we can avoid problems with indexes >9 being multiple characters
    # in the string
    file_index = ord('0')
    for c in data:
        if is_free:
            expanded_str += "."*int(c)
        else:
            expanded_str += chr(file_index)*int(c)
            file_index += 1
        is_free = not is_free
    print('Finished expanding string')
    return 'Not impl'

solution()