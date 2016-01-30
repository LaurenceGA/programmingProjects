#!/usr/bin/env python
from sys import stdout

__author__ = "Laurence"
authorship_string = "{} created on {} by {}\n{}\n".format(
    "d19.py", "19/12/2015", __author__, "-----" * 15) \
    if __name__ == '__main__' else ""
stdout.write(authorship_string)

import re

data = [line.rstrip() for line in open('inp.txt')]

med_molucule = ''

replacements = {}

for l in data:
    if l:
        m = re.match(R"(.+) => (.+)", l)
        if m:
            if m.group(1) in replacements:
                replacements[m.group(1)].append(m.group(2))
            else:
                replacements[m.group(1)] = [m.group(2)]
        else:
            med_molucule = l

# med_molucule = 'HOH'
# replacements = {
#     'H': ['HO', 'OH'],
#     'O': ['HH']
# }


def step(replac, mol):
    molecules = []
    for old, repl_list in replac.items():
        for rep in repl_list:
            found_index = 0
            while found_index >= 0:
                found_index = mol.find(old, found_index)
                if found_index >= 0:
                    molecules.append(mol[:found_index] + mol[found_index:].replace(old, rep, 1))
                    found_index += 1

    return molecules

reps = []
for k, v in replacements.items():
    for r in v:
        reps.append((k, r))

target = med_molucule
part2 = 0
from random import shuffle
while target != 'e':
    tmp = target
    for a, b in reps:
        if b not in target:
            continue

        target = target.replace(b, a, 1)
        part2 += 1

    if tmp == target:
        target = med_molucule
        part2 = 0
        shuffle(reps)

print(part2)

# print(len(set(molecules)))
# print(molecules)
