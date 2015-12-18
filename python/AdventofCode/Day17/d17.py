#!/usr/bin/env python
from sys import stdout

__author__ = 'Laurence Armstrong'
authorship_string = "{} created on {} by {} ({})\n{}\n".format(
        "d17.py", "17/12/15", __author__, 15062061, "-----" * 15) \
    if __name__ == '__main__' else ""
stdout.write(authorship_string)

import itertools

data = [line for line in open('inp.txt')]

data = [int(num) for num in data]

total_litres = 150

combos = []
for i in range(len(data)):
    c = itertools.combinations(data, i)
    combos += c

combs = 0
fitting_combos = []
for c in combos:
    if sum(c) == total_litres:
        fitting_combos.append(c)

print("Number of combos:", len(fitting_combos))
min_num = min([len(c) for c in fitting_combos])
print("Min containers:", min_num)
min_cont_ways = list(filter(lambda x: len(x) == min_num, fitting_combos))
print(len(min_cont_ways))