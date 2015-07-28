#!/usr/bin/env python
from sys import stdout

__author__ = 'Laurence Armstrong'
authorship_string = "{} created on {} by {} ({})\n{}\n".format(
    "fibbonacci.py", "28/07/15", __author__, 15062061, "-----" * 15) \
    if __name__ == '__main__' else ""
stdout.write(authorship_string)

def fibs(num):
    assert (num > 1), 'invalid parameter'
    result = [0, 1]
    for i in range(num -2):
        result.append(result[-2] + result[-1])
    return result

print fibs(10)
