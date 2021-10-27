from vectors import *
from transforms import *
from math import *


# Testing our infer_matrix() function:
x = infer_matrix(3, rotate_z_by(pi/2))
print(x)

# Testing random_matrix() function:
# A random 3x3 matrix with entries between 0 and 10:
print(random_matrix(3,3,0,10))

# Ex 5.10 
a = ((1,1,0), (1,0,1), (1,-1,1))
b = ((0,2,1), (0,1,0), (1,0,-1))

def transform_a(v):
    return multiply_matrix_vector(a, v)

def transform_b(v):
    return multiply_matrix_vector(b, v)

compose_a_b = compose(transform_a, transform_b)

print(infer_matrix(3, compose_a_b))
print(matrix_multiply(a, b))

transpose(((1, 2, 3),))

def project_xy(v):
    x,y,z = v
    return (x,y)

print(infer_matrix(3, project_xy))