#!/usr/bin/env python
from sys import stdout

__author__ = 'Laurence Armstrong'
authorship_string = "{} created on {} by {} ({})\n{}\n".format(
    "find_max.py", "22/10/15", __author__, 15062061, "-----" * 15) \
    if __name__ == '__main__' else ""
stdout.write(authorship_string)


def find_max(seq, max_so_far):
    if len(seq) == 1:
        return max_so_far if seq[0] < max_so_far else seq[0]
    if max_so_far >= seq[0]:
        return find_max(seq[1:], max_so_far)
    else:
        return find_max(seq[1:], seq[0])

seq = [7, 2, 4, 9, 1, 5, 3, 7, 3, 6]

print find_max(seq, seq[0])
