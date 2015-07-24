#!/usr/bin/env python
from sys import stdout
__author__ = 'Laurence Armstrong'
authorship_string = "{} created on {} by {} ({})\n{}\n".format(
    "main.py", "24/07/15", __author__, 15062061, "-----" * 15) \
    if __name__ == '__main__' else ""
stdout.write(authorship_string)

from vector import Vector
from matrix import Matrix

v = Vector(1, 2, 3, 4, 5)
u = Vector(0, 1, 2, 3, 4)
w = Vector(-1, -2, -3, -4, -5)
z = Vector(1, 2)

a = Matrix((1, 2, 3), (2, 3, 4))
