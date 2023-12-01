import re
def day4():
    data = open(r'Inputs\day4.in').read()[:-1].split('\n\n')
    print('Part 1 result: ' + str(part1(data)))
    print('Part 2 result: ' + str(part2(data)))

required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

def part1(data):
    valid = 0
    for x in data:
        x = x.split()
        # at this point all of fields for each passport are in x
        # next we split them all on the : and just take the first one since we don't care
        # about the values in this part
        passport = [y.split(':')[0] for y in x]
        # if all of the keys in required are in passport then its valid
        if all(key in passport for key in required):
            valid += 1
    return valid

def part2(data):
    valid = 0
    for passport in data:
        fields = re.split('[\n ]', passport)
        # dictionary of our fields for this passport
        d = dict(field.split(':') for field in fields)
        # if all of the keys in required are in d
        if all(key in d for key in required):
            # 1920 <= byr <= 2002
            # 2010 <= iyr <= 2020
            # 2020 <= eyr <= 2030
            # make sure hgt is 1 more or digits followed by 2 other characters
            # if hgt ends with cm check if its between 150 and 193
            # or if it ends with in check between 59 and 76
            # look for a # followed by exactly 6 characters 0-9 or a-f
            # make sure the eye color is one of the given ones
            # pid is exactly 9 digit characters
            # if we made it here then the passport is valid
            if 1920 <= int(d['byr']) <= 2002\
                and 2010 <= int(d['iyr']) <= 2020\
                and 2020 <= int(d['eyr']) <= 2030\
                and re.match(r'\d+..', d['hgt'])\
                and (d['hgt'].endswith('cm') and 150 <= int(d['hgt'][:-2]) <= 193 or d['hgt'].endswith('in') and 59 <= int(d['hgt'][:-2]) <= 76)\
                and re.match(r'^#[\da-f]{6}$', d['hcl'])\
                and d['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']\
                and re.match(r'^\d{9}$', d['pid']):
                valid += 1
    return valid

day4()