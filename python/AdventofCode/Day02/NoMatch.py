#!/usr/bin/env python
from sys import stdout

__author__ = "Laurence"
authorship_string = "{} created on {} by {}\n{}\n".format(
    "NoMatch.py", "13/12/2015", __author__, "-----" * 15) \
    if __name__ == '__main__' else ""
stdout.write(authorship_string)


def get_area(l, w, h):
    s1 = l*w
    s2 = w*h
    s3 = h*l
    return 2*(s1 + s2 + s3) + min(s1, s2, s3)


def get_ribbon(l, w, h):
    return 2*(l + w + h) - 2*max(l, w, h) + l*w*h

with open('inp.txt') as f:
    raw_data = f.readlines()
    data = [list(map(int, x.strip().split('x'))) for x in raw_data]

total_area = 0
total_ribbon = 0
for p in data:
    total_area += get_area(*p)
    total_ribbon += get_ribbon(*p)

print("Area: {} feet^2".format(total_area))
print("Length: {} feet".format(total_ribbon))
