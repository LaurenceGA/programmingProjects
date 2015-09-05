#!/usr/bin/env python
__author__ = 'Laurence Armstrong'
authorship_string = "{} created on {} by {} ({})\n{}\n".format(
    "test.py", "21/07/2015", __author__, 15062061, "-----" * 15) \
    if __name__ == '__main__' else ""
print authorship_string,


def odd(n):
    if n <= 1:
        return 1
    return n*even(n-1)

def even(n):
    return n*odd(n-1)

print odd(5)
