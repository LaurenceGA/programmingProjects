#!/usr/bin/env python
from sys import stdout
__author__ = 'Laurence Armstrong'
authorship_string = "{} created on {} by {} ({})\n{}\n".format(
    "vector.py", "15/07/15", __author__, 15062061, "-----" * 15) \
    if __name__ == '__main__' else ""
stdout.write(authorship_string)


class Vector(object):
    # Initialize vector
    def __init__(self, *elements):
        self.elements = list(elements)

        self.index = 0      # Iteration index start

    # FOLLOWING FUNCTION DEFINE BUILT IN OPERATIONS ON VECTORS
    def __iter__(self):
        """
        Make the vector iterable
        """
        return self

    def next(self):
        """
        Access next item
        """
        if self.index == len(self.elements):
            self.index = 0
            raise StopIteration

        self.index += 1

        return self.elements[self.index - 1]

    def __str__(self):
        """
        How to print the vector
        """
        return str(self.elements)

    def __len__(self):
        """
        Length of the vector returns number of elements
        """
        return len(self.elements)

    def __getitem__(self, item):
        """
        Indexing. v[i] returns index at i
        """
        return self.elements[item]

    def __setitem__(self, key, value):
        """
        Set v[key] = value
        """
        self.elements[key] = value

    def __add__(self, other):
        """
        Defines v + u as v.add(u)
        """
        return self.add(other)

    def __sub__(self, other):
        """
        Defines v - u as v.subtract(u)
        """
        return self.subtract(other)

    def __mul__(self, other):
        """
        Defines v * const as v.scale(const) where const is int or float
        """
        # print other
        if type(other) == int or type(other) == float:
            return self.scale(other)
        elif type(other) == Vector:
            return self.dot(other)
        else:
            return NotImplemented

    def __rmul__(self, other):
        """
        defines const * v as v.scale(const) where const is int or float
        """
        if type(other) == int or type(other) == float:
            return self.scale(other)
        else:
            return NotImplemented

    def __neg__(self):
        return self.scale(-1)

    def __nonzero__(self):
        for e in self:
            if e != 0:
                return True
        return False

    # VECTOR MANIPULATION FUNCTIONS
    def reset(self):
        """
        Set all elements to 0
        """
        self.elements = [0] * len(self)

    def add(self, vec2):
        """
        Add two vectors together
        """
        if type(vec2) != Vector:
            raise TypeError("Not a vector")

        if len(vec2) != len(self):
            raise DifferentLengthVectors(self, vec2)

        return Vector(*[self[i]+vec2[i] for i in range(len(self))])

    def subtract(self, vec2):
        """
        Subtract one vector from this one
        """
        if type(vec2) != Vector:
            raise TypeError("Not a vector")

        if len(vec2) != len(self):
            raise DifferentLengthVectors(self, vec2)

        return Vector(*[self[i]-vec2[i] for i in range(len(self))])

    def scale(self, const):
        """
        Scale vector by a constant
        """
        return Vector(*[self[i]*const for i in range(len(self))])

    def dot(self, vec2):
        """
        Return the dot product of two vectors
        """
        if type(vec2) != Vector:
            raise TypeError("Not a vector")

        if len(vec2) != len(self):
            raise DifferentLengthVectors(self, vec2)

        return sum([self[i]*vec2[i] for i in range(len(self))])

    def len(self):
        """
        Return the length of the vector. Not # of elements
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
        if type(vec2) != Vector:
            raise TypeError("Not a vector")

        return (self - vec2).len()

    def angle(self, vec2):
        """
        Return angle between two vectors in radians
        return math.Acos(v1.Dot(v2) / (v1.Len() * v2.Len()))
        """
        if type(vec2) != Vector:
            raise TypeError("Not a vector")

        from math import acos
        return acos(self.dot(vec2) / (self.len() * vec2.len()))

    def cross(self, vec2):
        """
        Return the cross product of two vectors
        """
        if type(vec2) != Vector:
            raise TypeError("Not a vector")

        if (len(self) or len(vec2)) != 3:
            raise Exception("Incorrect vector lengths. Must be two 3 length vectors.")

        return Vector(self[1]*vec2[2] - self[2]*vec2[1],
                      self[2]*vec2[0] - self[0]*vec2[2],
                      self[0]*vec2[1] - self[1]*vec2[0])


class DifferentLengthVectors(Exception):
    def __init__(self, vec1, vec2):
        self.vec1 = vec1
        self.vec2 = vec2

    def __str__(self):
        return "These vectors must be of same length. " \
               "Vector 1 is of length {}, vector 2 is of length {}".format(len(self.vec1), len(self.vec2))
