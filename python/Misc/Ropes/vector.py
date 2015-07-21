#!/usr/bin/env python
__author__ = 'Laurence Armstrong'
authorship_string = "{} created on {} by {} ({})\n{}\n".format(
    "vector.py", "15/07/15", __author__, 15062061, "-----" * 15) \
    if __name__ == '__main__' else ""
print(authorship_string, end="")


class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    def reset(self):
        """
        Set x and y to 0
        """
        self.x = 0
        self.y = 0

    def add(self, vec2):
        """
        Add two vectors together
        """
        return Vector(self.x + vec2.x, self.y + vec2.y)

    def subtract(self, vec2):
        """
        Subtract one vector from this one
        """
        return Vector(self.x - vec2.x, self.y - vec2.y)

    def scale(self, const):
        """
        Scale vector by a constant
        """
        return Vector(self.x * const, self.y * const)

    def dot(self, vec2):
        return (self.x * vec2.x) + (self.y * vec2.y)

    def len(self):
        """
        Return the length of the vector
        """
        return (self.dot(self))**0.5

    def normalize(self):
        """
        Return the unit vector
        """
        l = 1 / self.len()
        return self.scale(l)

    def dist(self, vec2):
        """
        Return the distance to another vector
        """
        return self.subtract(vec2).len()

    def angle(self, vec2):
        """
        Return angle between two vectors in radians
        return math.Acos(v1.Dot(v2) / (v1.Len() * v2.Len()))
        """
        from math import acos
        return acos(self.dot(vec2) / (self.len() * vec2.len()))