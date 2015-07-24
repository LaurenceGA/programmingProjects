#!/usr/bin/env python
from sys import stdout
__author__ = 'Laurence Armstrong'
authorship_string = "{} created on {} by {} ({})\n{}\n".format(
    "matrix.py", "24/07/15", __author__, 15062061, "-----" * 15) \
    if __name__ == '__main__' else ""
stdout.write(authorship_string)

from vector import Vector


class Matrix(object):
    # Initialize matrix
    def __init__(self, *elements):
        self.elements = []
        for element in elements:
            self.elements.append(Vector(*element))

        print self

    # FOLLOWING FUNCTION DEFINE BUILT IN OPERATIONS ON MATRICIES
    def __str__(self):
        """
        Correctly print the matrix
        """
        to_string = "["
        for e in self.elements:
            for i in e:
                to_string += str(i) + ' '
            to_string += '\n '
        to_string = to_string[:-3] + ']'
        return to_string

    """
    TODO
    iteration
    """

    # MATRIX MANIPULATION FUNCTIONS
    """
    TODO
    echelon
    RREF
    Row operations
        -Add
        -Scale
        -Move
    Get (row, column)
    Set (row, column)
    Multiply matricies
    Multiply vector
    Determinant
    Transpose
    """

