import collections, time
def day4p1():
    lower=372037
    upper=905157
    valid=0
    for num in range(lower, upper):
        if(is_valid_pass(num, lower, upper)):
            valid += 1

    return valid

def day4p2():
    lower=372037
    upper=905157
    valid=0
    for num in range(lower, upper):
        if(is_valid_pass_p2(num, lower, upper)):
            valid += 1

    return valid

def is_valid_pass(num, lower, upper):
    if(len(str(num)) != 6):
        return False
    if(num < lower or num > upper):
        return False
    strnum = str(num)
    lastnum = strnum[0]
    nums = set()
    double = False
    for c in strnum:
        if int(c) < int(lastnum):
            return False
        if c in nums:
            double = True
            lastnum = c
        else:
            nums.add(c)
            lastnum = c
    return double

def is_valid_pass_p2(num, lower, upper):
    if(len(str(num)) != 6):
        return False
    if(num < lower or num > upper):
        return False
    strnum = str(num)
    lastnum = strnum[0]
    cnt = collections.Counter()
    for c in strnum:
        if int(c) < int(lastnum):
            return False
        cnt[c] += 1
        lastnum = c
    counts = cnt.most_common()
    for count in counts:
        if count[1] == 2:
            return True
    return False

start_time = time.time()
print(day4p1())
print(day4p2())
end_time = time.time()
total_time = end_time - start_time
print("Total time: " + str(total_time) + " seconds")