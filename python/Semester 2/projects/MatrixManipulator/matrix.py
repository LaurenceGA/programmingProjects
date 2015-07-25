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
        self.index = 0
        return self

    def next(self):
        """
        Access next item
        """
        if self.index == len(self.elements):
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
                if int(i) == i:
                    i = str(int(i))
                else:
                    i = "{:.2f}".format(i)

                to_string += i + ' '
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
        if type(other) == int or type(other) == float:
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
        if type(other) == int or type(other) == float:
            return self.scale(other)
        elif type(other) == Vector:
            return self.multiply(Matrix(other).transpose())
        else:
            return NotImplemented

    def __neg__(self):
        return self * -1

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

    def determinant(self):
        """
        Find the determinant of the matrix
        """
        if self.row_num() != self.col_num():
            raise NotSquareError("The matrix must be square to find the determinant")

        if len(self) == 2:
            # ad - bc
            return self[0][0]*self[1][1] - self[1][0]*self[0][1]
        else:
            return -1

    # Elementary row operations
    def row_add(self, i, j, scale=1):
        """
        Add row i to j
        """
        self[j] += self[i] * scale

    def row_scale(self, i, const):
        """
        Scale row i by const
        """
        if i >= len(self):
            raise DimensionError("Row does not exist")

        self[i] = self[i].scale(const)

    def row_switch(self, i, j):
        """
        Switch row i with row j
        """
        if i == j:
            return
        self[i], self[j] = self[j], self[i]

    def invert(self):
        """
        Return the inverted version of a matrix
        invert (2x2, 1/(ad - bc) * (d -b, -c a)) detA = 0 = not invertible
        """
        if self.row_num() != self.col_num():
            raise NotSquareError("Matrix must be square to invert")

        det = self.determinant()

        if det == 0:    # Would be divided by 0
            raise ZeroDivisionError("Matrix is not invertible")

        if len(self) == 2:
            return Matrix((self[1][1], -self[0][1]), (-self[1][0], self[0][0])).scale(1 / det)

    def echelon(self):
        # Order it as much as possible first
        cur_row = 0
        cur_col = 0
        while cur_row < len(self):
            if cur_col >= len(self[0]):
                break
            for row in range(cur_row, len(self)):   # Go down columns
                if self[row][cur_col] != 0:
                    self.row_switch(cur_row, row)

                    # Make everything below 0
                    for r in range(row + 1, len(self)):
                        # self.row_add(row, r, -(self[row][cur_col]) * self[r][cur_col])
                        self.row_add(row, r, -(self[r][cur_col] / self[row][cur_col]))

                    cur_row += 1
                    # cur_col += 1

                    break
            cur_col += 1

    def rref(self):
        self.echelon()
        cur_row = 0
        cur_col = 0
        while cur_row < len(self):
            if cur_col >= len(self[0]):
                break
            for row in range(cur_row, len(self)+1):   # Go down columns
                if row == len(self):
                    if self[row-1][cur_col-1] == 0:
                        self.row_scale(row-1, 1/float(self[row-1][cur_col]))

                        if row-2 >= 0:
                            for r in range(row-2, -1, -1):
                                self.row_add(row-1, row-2, -(self[row-2][cur_col]))

                        cur_row += 1

                        break
                    else:
                        break
                if self[row][cur_col] == 0:
                    if row == 0:
                        break

                    # if not self[row]:
                    #     return

                    if row-1 >= 0:
                        if self[row-1][cur_col] == 0:
                            break
                        if cur_col >= 1:
                            if self[row-1][cur_col-1] != 0:
                                break

                    self.row_scale(row-1, 1 / float(self[row-1][cur_col]))

                    if row-2 >= 0:
                        for r in range(row-2, -1, -1):
                            self.row_add(row-1, r, -(self[row-2][cur_col]))

                    cur_row += 1

                    break

            cur_col += 1

    """
    TODO
    invert of > 2x2
    Determinant of > 2x2 (co-factor expansion)
    """


class DimensionError(Exception):
    def __init__(self, value):
        self. value = value

    def __str__(self):
        return "Incorrect matrix dimensions{}".format("; {}".format(self.value))


class NotSquareError(DimensionError):
    def __init__(self, value):
        self. value = value

    def __str__(self):
        return "The matrix is not square{}".format("; {}".format(self.value))
