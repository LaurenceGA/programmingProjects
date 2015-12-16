#!/usr/bin/env python
from sys import stdout

__author__ = "Laurence"
authorship_string = "{} created on {} by {}\n{}\n".format(
    "KnightsOfTable.py", "14/12/2015", __author__, "-----" * 15) \
    if __name__ == '__main__' else ""
stdout.write(authorship_string)

import re
import itertools

guest_happiness = [line.rstrip() for line in open('inp.txt')]


class Guest(object):
    def __init__(self):
        self.neighbours = {"": 0}

    def __str__(self):
        return str(self.neighbours)

guests = {"": Guest()}

for gh in guest_happiness:
    m = re.match(R'(.+) would (.+) (\d+) happiness units by sitting next to (.+)\.', gh)

    if m.group(1) not in guests:
        guests[m.group(1)] = Guest()
    if m.group(4) not in guests:
        guests[m.group(4)] = Guest()

    sign = 1 if m.group(2) == 'gain' else -1

    guests[m.group(1)].neighbours[m.group(4)] = sign*int(m.group(3))

for g in guests:
    if g != "":
        guests[""].neighbours[g] = 0


def get_happy(arrangement, guests):
    dHappy = 0
    for i, g in enumerate(arrangement):
        if i == 0:
            dHappy += guests[g].neighbours[arrangement[-1]] + guests[g].neighbours[arrangement[i+1]]
        elif i == len(arrangement)-1:
            dHappy += guests[g].neighbours[arrangement[i-1]] + guests[g].neighbours[arrangement[0]]
        else:
            dHappy += guests[g].neighbours[arrangement[i-1]] + guests[g].neighbours[arrangement[i+1]]
    return dHappy

dhap = []
for i in list(itertools.permutations(guests)):
    dhap.append(get_happy(i, guests))

print(max(dhap))