#!/usr/bin/env python
from sys import stdout

__author__ = "Laurence"
authorship_string = "{} created on {} by {}\n{}\n".format(
    "LookSay.py", "14/12/2015", __author__, "-----" * 15) \
    if __name__ == '__main__' else ""
stdout.write(authorship_string)


inp = '1321131112'
# 11131221133112


def lookSay(num):
    cur_num = None
    count = 1
    new_seq = ''

    for i, c in enumerate(num):
        if cur_num is None:
            cur_num = c
            count = 1
        elif c == cur_num:
            count += 1
        else:
            new_seq += str(count) + cur_num
            count = 1
            cur_num = c
        if i == len(num)-1:
                new_seq += str(count) + cur_num

    return new_seq

for i in range(50):
    inp = lookSay(inp)

print(inp)
print(len(inp))
