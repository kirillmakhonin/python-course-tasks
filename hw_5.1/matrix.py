#!/usr/bin/env python3
import random

class MatrixError(Exception):
    """Matrix Exception"""
    pass

class Matrix():
    def __init__(cls, *args):
        """
        init Matrix with (m, n) where m - rows, n - columns
        Matrix(2, 1)
        [[0, 7]]

        or with list of rows
        Matrix([[0, 1], [2 ,3]])
        [[0, 1],
        [2, 3]]

        """
        if len(args) == 2: # init matrix with (m, n) m rows with n random numbers(0-10)
            self.rows = [[random.randomint(0, 10) for n in range(args[1])] for m in range(args[0])]
            self.m = args[0]
            self.n = args[1]
        elif len(args) == 1: 
            rows = args[0]
            if any([len(row) != n for row in rows[1:]]):
                raise MatrixError("inconsistent row length")
            self.m = len(rows)
            self.n = len(rows[0])
            self.rows = args[0]
        else:
            raise MatrixError('Init matrix with (m, n):rows, columns or [[1,2], [2, 4]]')
        

    m = len(rows)
    n = len(rows[0])
    # Validity check
    if any([len(row) != n for row in rows[1:]]):
        raise MatrixError, "inconsistent row length"
    mat = Matrix(m,n, init=False)
    mat.rows = rows

return mat
