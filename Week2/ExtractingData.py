import re

hand = open('Regex_sum_1237186.txt')

n = list()
for line in hand:
     x = re.findall('[0-9]+',line)
     n = n + x

sum = 0
for i in n:
    sum = sum + int (i)

print(sum)