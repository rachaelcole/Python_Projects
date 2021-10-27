from vectors import *
from math import *
from draw_model import *
from transforms import *
from teapot import *
from draw_teapot import load_triangles

"""
Any linear transformation in 3D can be specified by 3 vectors, or 9 numbers, called a matrix.

The transformation "rotate counterclockwise by 90 degrees about the z-axis" can be described by what it
does to the standard basis vectors: e1 = (1,0,0), e2 = (0,1,0) and e3 = (0,0,1)

Written as a matrix the standard basis vectors are:

e = (1, 0, 0
     0, 1, 0
     0, 0, 1)

A matrix lets us compute any given linear transformation using the data of what that transformation does to
the standard basis vectors.

Suppose A is a linear transformation. We know:
    A(e1) = (1, 1, 1)
    A(e2) = (1, 0, -1)
    A(e3) = (0, 1, 1)
These three vectors are all we need to specify the linear transformation A.
Written as a single column matrix (representing a vector):
A = (1  1  0
     1  0  1
     1 -1  0)

In 2D, a column vector consists of two entities, making a square matrix (representing a linear transformation):
D(e1) = (2, 0) 
D(e2) = (0, 2)
Written as a square matrix:
D = (2, 0
     0, 2)

To get a matrix from a linear transformation, find the vectors it produces from the standard basis vectors,
and combine the results side-by-side.
"""


# Multiplying a matrix by a vector

# Linear transformation matrix 'B':
B = (  
    (0, 2, 1),
    (0, 1, 0),
    (1, 0, -1)
)

# Vector 'v':
v = (3, -2, 5)

# To get the columns of B, use zip()
columns_of_B = list(zip(*B))
print(columns_of_B)

print(multiply_matrix_vector(B,v))

# 5.1.3
A = (
    (1, 1, 0),
    (1, 0, 1),
    (1, -1, 1)
)

Bv = (
    (0, 2, 1),
    (0, 1, 0),
    (1, 0, -1)
)

# Multiply two matrices:
def matrix_multiply(a,b):
    return tuple(
        tuple(dot(row, col) for col in zip(*b)) 
        for row in a
    )

print(f'A times Bv is {matrix_multiply(A, Bv)}')
ABv = (
    (0, 3, 1),
    (1, 2, 0),
    (1, 1, 0)
)

# Multiply two 2D vectors as square matrices:
c = ((1,2), (3,4))
d = ((0,-1), (1,0))
print(f'c times d is {matrix_multiply(c,d)}')

# We can use pygame's built in Clock to generate matrices depending on time
# So every entry of the matrix is a function that takes the current time (t)
# and returns a number. We can use sin/cos functions in our matrix to represent
# rotate_y_by(t):
# (
#   (cos(t), 0, -sin(t)),
#   (0,      1,    0   ),
#   (sin(t), 0, cos(t))
# )

def get_rotation_matrix(t):  # Generates new transformation matrix for any numeric input representing time
    seconds = t/1000  # Convert time to seconds
    return (
        (cos(seconds), 0, -sin(seconds)),
        (0, 1, 0),
        (sin(seconds), 0, cos(seconds))
        )

# Pass the get_rotation_matrix function as an argument in the draw_model() function
draw_model(load_triangles(), get_matrix=get_rotation_matrix)  # Output is a spinning teapot

# Infer a matrix from a dimension and a linear transformation:
def infer_matrix(n, transformation):
    def standard_basis_vector(i):
        return tuple(1 if i==j else 0 for j in range(1, n+1))  # Create ith standard basis vector
    standard_basis = [standard_basis_vector(i) for i in range(1, n+1)]  # Create standard basis as a list of n vectors
    cols = [transformation(v) for v in standard_basis]  # Define the columns of the matrix by applying the linear transformations to the vectors
    return tuple(zip(*cols))  # Reshapes the matrix to be a tuple of rows

# Testing our infer_matrix() function:
x = infer_matrix(3, rotate_z_by(pi/2))
print(x)

