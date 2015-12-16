#!/usr/bin/env python
from sys import stdout

__author__ = "Laurence"
authorship_string = "{} created on {} by {}\n{}\n".format(
    "Matchsticks.py", "14/12/2015", __author__, "-----" * 15) \
    if __name__ == '__main__' else ""
stdout.write(authorship_string)

strings = [line.rstrip() for line in open('inp.txt')]

print(sum(2+s.count('\\')+s.count('"') for s in open('inp.txt')))

code_chars = 0
mem_chars = 0

for s in strings:
    code_chars += len(s)
    mem_chars += len(eval(s))

print(code_chars - mem_chars)
