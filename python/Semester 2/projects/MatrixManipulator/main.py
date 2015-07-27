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
b = Matrix((0, 1, 2), (1, 2, 3))
c = -a
d = Matrix((1, 2, 3), (2, 3, 4), (5, 6, 7))
e = Matrix((1, 2), (3, 4), (5, 6))
f = Matrix((1, 2), (3, 4))
g = Matrix((8, 0, 0, 0), (0, 0, 1, 5), (3, 0, 1, 1), (5, 10, 0, 2))
h = Matrix((0, 0, 0), (0, 1, 5), (3, 1, 1))
i = Matrix((0, 0, 0), (0, 0, 0), (0, 0, 0))
j = Matrix((5, 8, 3, 4, 0),
           (5, 9, 4, 4, 8),
           (4, 11, 15, 4, 7),
           (1, 0, 0, 4, 3),
           (6, 4, 12, 0, 1))

m = d

print m.determinant()
# print m
# print
# m.rref()
# print m.determinant()
# n = m.invert()
# print n
# print
# print n * m
