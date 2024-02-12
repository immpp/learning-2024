import re

file = open('regex_sum_1972780.txt')
fsum = 0
lnum = []

for line in file:
    fnum = re.findall('[0-9]+', line)
    if len(fnum) > 0:
        for num in fnum:
            lnum.append(num)

for num in lnum:
    inum = int(num)
    fsum = fsum + inum

print(fsum)