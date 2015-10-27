#!/usr/bin/env python
from sys import stdout

__author__ = 'Laurence Armstrong'
authorship_string = "{} created on {} by {} ({})\n{}\n".format(
    "palllendrome.py", "22/10/15", __author__, 15062061, "-----" * 15) \
    if __name__ == '__main__' else ""
stdout.write(authorship_string)


def is_palindrome(alist):
    if len(alist) < 2:
        return True
    elif len(alist) == 2:
        return alist[0] == alist[1]
    elif alist[0] == alist[-1]:
        return is_palindrome(alist[1:-1])
    else:
        return False

print is_palindrome(list("tacocat"))
