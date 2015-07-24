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
        vec_len = len(elements[0])
        for element in elements:
            if len(element) != vec_len:
                raise DimensionError("Matrix cannot be created")
            self.elements.append(Vector(*element))

        self.index = 0  # Iteration start index

    # FOLLOWING FUNCTION DEFINE BUILT IN OPERATIONS ON MATRICIES
    def __iter__(self):
        """
        Make the matrix iterable
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
        Correctly print the matrix
        """
        to_string = "["
        for e in self.elements:
            for i in e:
                to_string += str(i) + ' '
            to_string += '\n '
        to_string = to_string[:-3] + ']'
        return to_string

    def __len__(self):
        """
        How many vectors long the matrix is
        """
        return len(self.elements)

    def __getitem__(self, item):
        """
        Return vector at position item
        """
        return self.elements[item]

    def __setitem__(self, key, value):
        """
        Set vector as position key to value
        """
        if type(value) != Vector:
            raise TypeError("Not a vector")
        self.elements[key] = value

    def __add__(self, other):
        return self.add(other)

    def __sub__(self, other):
        return self.subtract(other)

    def __mul__(self, other):
        """
        Defines A * const as A.scale(const) where const is int or float
        """
        if type(other) == (int or float):
            return self.scale(other)
        elif type(other) == Matrix:
            return self.multiply(other)
        elif type(other) == Vector:
            return self.multiply(Matrix(other).transpose())
        else:
            return NotImplemented

    def __rmul__(self, other):
        """
        defines const * A as A.scale(const) where const is int or float
        """
        if type(other) == (int or float):
            return self.scale(other)
        elif type(other) == Vector:
            return self.multiply(Matrix(other).transpose())
        else:
            return NotImplemented

    # MATRIX MANIPULATION FUNCTIONS
    def reset(self):
        """
        Set matrix equal to identity matrix if it's square
        """
        if self.row_num() != self.col_num():
            raise NotSquareError

        for i in range(len(self)):
            self[i] = Vector(*[1 if i == j else 0 for j in range(len(self))])

    def transpose(self):
        m_list = []
        for i in range(self.col_num()):
            v_list = []
            for j in range(self.row_num()):
                v_list.append(self[j][i])
            m_list.append(Vector(*v_list))

        return Matrix(*m_list)

    def row_num(self):
        """
        Returns the number of rows in the matrix
        """
        return len(self.elements)

    def col_num(self):
        """
        Returns the number of columns in the matrix
        """
        return len(self.elements[0])

    def get_element(self, row, column):
        """
        Get element A[row][column]
        """
        return self[row][column]

    def set_element(self, row, column, value):
        """
        Set element A[row][column] = value
        """
        self.elements[row][column] = value

    def scale(self, const):
        """
        Scale a whole matrix by a constant
        """
        return Matrix(*[vect.scale(const) for vect in self.elements])

    def add(self, b):
        """
        Add b to self where b is another matrix
        """
        if type(b) != Matrix:
            raise TypeError("Not a matrix")

        if self.row_num() != b.row_num() or self.col_num() != b.col_num():
            raise DimensionError

        m_list = []
        for v in range(len(self)):
            m_list.append(self[v] + b[v])

        return Matrix(*m_list)

    def subtract(self, b):
        """
        Subtract b from self where b is another matrix
        """
        if type(b) != Matrix:
            raise TypeError("Not a matrix")

        if self.row_num() != b.row_num() or self.col_num() != b.col_num():
            raise DimensionError

        m_list = []
        for v in range(len(self)):
            m_list.append(self[v] - b[v])

        return Matrix(*m_list)

    def multiply(self, b):
        if type(b) != Matrix:
            raise TypeError("Not a matrix")

        if self.col_num() != b.row_num():
            raise DimensionError("Col(A) must equal row(B)")

        m_list = []
        for r in range(self.row_num()):
            new_vect = []
            for v in range(b.col_num()):
                v_list = []
                for i in range(b.row_num()):
                    v_list.append(b[i][v])
                col_vector = Vector(*v_list)
                new_vect.append(self[r] * col_vector)
            m_list.append(Vector(*new_vect))

        return Matrix(*m_list)

    """
    TODO
    echelon
    RREF
    Row operations
        -Add
        -Scale
        -Move
    invert (2x2, 1/(ad - bc) * (d -b, -c a)) detA = 0 = not invertible
    Determinant
    co-factor expansion
    """


class DimensionError(Exception):
    def __str__(self):
        return "Incorrect matrix dimensions"


class NotSquareError(DimensionError):
    def __str__(self):
        return "The matrix is not square"
