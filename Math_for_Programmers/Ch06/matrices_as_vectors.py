import numpy as np
import matplotlib.pyplot as plt
from math import sin
from classes import *
from colors import *
from functions_as_vectors import *
from matrices import *
from tests import *
from vectors import *


# Matrix lass inheriting from Vector 
class Matrix(Vector):
    @abstractproperty
    def rows(self):
        pass
    @abstractproperty
    def columns(self):
        pass
    def __init__(self, entries):
        self.entries = entries
    def add(self, other):
        return self.__class__(tuple(tuple(self.entries[i][j] + other.entries[i][j] 
        for j in range(0,self.columns())) for i in range(0,self.rows())))
    def scale(self, scalar):
        return self.__class__(tuple(tuple(scalar * e for e in row) 
        for row in self.entries))
    def __repr__(self):
        return (f'{self.__class__.__qualname__}{self.entries}')
    def zero(self):
        return self.__class__(
            tuple(
                tuple(0 for i in range(0,self.columns())) 
                for j in range(0, self.rows())))



# A class representing 5x3 matrices thought of as vectors
class Matrix5_by_3(Matrix):
    def rows(self):
        return 5
    def columns(self):
        return 3

# 2x2 matrix:
class Matrix2_by_2(Matrix):
    def rows(self):
        return 2
    def columns(self):
        return 2



# Unit testing for 5x3 matrixes

# Define funcs for random inputs:
def random_matrix(rows, columns):
    return tuple(
        tuple(uniform(-10,10) for j in range(0,columns))
        for i in range(0, rows))

def random_5_by_3():
    return Matrix5_by_3(random_matrix(5,3))

def approx_equal_matrix_5_by_3(m1,m2):
    return all([
        isclose(m1.matrix[i][j], m2.matrix[i][j])
        for j in range(0,3) for i in range(0,5)])

# Run the test
"""
for i in range(0,100):
    a,b = random_scalar(), random_scalar()
    u,v,w = random_5_by_3(), random_5_by_3(), random_5_by_3()
    test(Matrix5_by_3.zero(), approx_equal_matrix_5_by_3, a,b,u,v,w)
"""