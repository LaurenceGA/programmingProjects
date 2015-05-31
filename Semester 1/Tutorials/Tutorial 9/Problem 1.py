#!/usr/bin/env python
__author__ = 'Laurence Armstrong'
authorship_string = "{} created on {} by {} ({})\n{}\n".format(
    "Problem 1.py", "18/05/15", __author__, 15062061, "-----" * 15) \
    if __name__ == '__main__' else ""
print(authorship_string, end="")

x_count = 0


def x():
    global x_count
    x_count += 1
    print("Called {} times".format(x_count))

for i in range(100):
    x()