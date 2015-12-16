#!/usr/bin/env python
from sys import stdout

__author__ = "Laurence"
authorship_string = "{} created on {} by {}\n{}\n".format(
    "d16.py", "16/12/2015", __author__, "-----" * 15) \
    if __name__ == '__main__' else ""
stdout.write(authorship_string)

import re

mfcsam_out = {'children': 3,
              'cats': 7,
              'samoyeds': 2,
              'pomeranians': 3,
              'akitas': 0,
              'vizslas': 0,
              'goldfish': 5,
              'trees': 3,
              'cars': 2,
              'perfumes': 1}

inp_lines = [line.rstrip() for line in open('inp.txt')]

sues = []

i = 1
for l in inp_lines:
    m = re.match(R'Sue (\d+): (.+: \d+,?)+', l)
    things = m.group(2).split(',')
    things_dict = {}
    for t in things:
        pair = t.split(':')
        things_dict[pair[0].strip()] = int(pair[1])
    sues.append((i, things_dict))
    i += 1

not_sue = []
for s in sues:
    for item in mfcsam_out:
        if item in s[1]:
            if item in ['cats', 'trees']:
                if not mfcsam_out[item] < s[1][item]:
                    not_sue.append(s[0])
                    break
            elif item in ['pomeranians', 'goldfish']:
                if not mfcsam_out[item] > s[1][item]:
                    not_sue.append(s[0])
                    break
            elif mfcsam_out[item] != s[1][item]:
                not_sue.append(s[0])
                break

for s in sues:
    if s[0] not in not_sue:
        print(s)
