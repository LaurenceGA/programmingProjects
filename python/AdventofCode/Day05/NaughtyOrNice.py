#!/usr/bin/env python
from sys import stdout

__author__ = "Laurence"
authorship_string = "{} created on {} by {}\n{}\n".format(
    "NaughtyOrNice.py", "13/12/2015", __author__, "-----" * 15) \
    if __name__ == '__main__' else ""
stdout.write(authorship_string)


lines = [line.rstrip() for line in open('inp.txt')]

nice = 0
"""
OLD RULES
for l in lines:
    has_double = False
    vowels = 0
    for i, char in enumerate(l):
        if char in 'aeiou':
            vowels += 1

        if i < len(l)-1 and not has_double:
            if char == l[i+1]:
                has_double = True
    if has_double and vowels >= 3 and 'ab' not in l and 'cd' not in l and 'pq' not in l and 'xy' not in l:
        nice += 1
"""

for l in lines:
    has_betweeen_repeat = False
    has_overlap = False
    for i in range(len(l)):
        if i < len(l)-2 and not has_betweeen_repeat:
            if l[i] == l[i+2]:
                has_betweeen_repeat = True

        if i < len(l)-2 and not has_overlap:
            if l[i:i+2] in l[i+2:]:
                has_overlap = True

    if has_betweeen_repeat and has_overlap:
        nice += 1

print(nice)
