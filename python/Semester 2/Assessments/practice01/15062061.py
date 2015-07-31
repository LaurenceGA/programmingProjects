#!/usr/bin/env python
from sys import stdout
__author__ = 'Laurence Armstrong'
authorship_string = "{} created on {} by {} ({})\n{}\n".format(
    "15062061.py", "31/07/2015", __author__, 15062061, "-----" * 15) \
    if __name__ == '__main__' else ""
stdout.write(authorship_string)

def countdown(n):
    for i in range(n):
        print i,
    print
    if n == 0:
        return
    countdown(n-1)

# countdown(10)

def reverse_cumulative(alist):
    result = []
    for i in range(len(alist)-1, -1, -1):
        if i == len(alist)-1:
            result.append(alist[i])
        else:
            result.append(result[len(alist) - (i+2)] + alist[i])
    return result

# print reverse_cumulative([1, 2, 3, 4, 5, 6])

def threes_list(n):
    return [i for i in range(3, n, 3)]

# print threes_list(15)

def rec_reverse(astring):
    if not astring:
        return
    rec_reverse(astring[1:])
    print astring[0]

rec_reverse("Hello!")
