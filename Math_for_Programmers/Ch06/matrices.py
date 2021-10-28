from vectors import *
from random import randint  

# Multiply a matrix by a vector:
def multiply_matrix_vector(matrix, vector):
    # return linear_combination(vector, *zip(*matrix))
    return tuple(
        dot(row, vector)
        for row in matrix
        )

# Multiply two matrices:
def matrix_multiply(a,b):
    return tuple(
        tuple(dot(row, col) for col in zip(*b)) 
        for row in a
    )

# Infer a matrix from a dimension and a linear transformation:
def infer_matrix(n, transformation):
    def standard_basis_vector(i):
        return tuple(1 if i==j else 0 for j in range(1, n+1))  # Create ith standard basis vector
    standard_basis = [standard_basis_vector(i) for i in range(1, n+1)]  # Create standard basis as a list of n vectors
    cols = [transformation(v) for v in standard_basis]  # Define the columns of the matrix by applying the linear transformations to the vectors
    return tuple(zip(*cols))  # Reshapes the matrix to be a tuple of rows

# Generate a random matrix:
def random_matrix(rows, cols, min=-2, max=2):
    return tuple(
        tuple(
            randint(min, max) for j in range(0, cols)
        ) for i in range(0, rows)
    )

# Raises a matrix to a specified power
def matrix_power(power, matrix):
    result = matrix
    for _ in range(1, power):
        result = matrix_multiply(result, matrix)
    return result

# Transpose a matrix
def transpose(matrix):
    return tuple(zip(*matrix))

# Take a translation vector and return a new function that applies that translation
# to a 3D vector:
def translate_3d(translation):
    def new_function(target):
        a,b,c = translation
        x,y,z = target
        matrix = ((1,0,0,a),(0,1,0,b),(0,0,1,c),(0,0,0,1))  # Build a 4x4 matrix for the translation
        vector = (x,y,z,1)  # Turn (x,y,z) into a 4D vector
        x_out, y_out, z_out, _ = multiply_matrix_vector(matrix, vector)  # Do the 4D matrix transformation
        return (x_out, y_out, z_out)
    return new_function

# Uses a 5x5 matrix to translate a 4D vector by another 4D vector:
def translate_4d(translation):
    def new_function(target):
        a,b,c,d = translation
        x,y,z,w = target
        matrix = (
            (1,0,0,0,a),
            (0,1,0,0,b),
            (0,0,1,0,c),
            (0,0,0,1,d),
            (0,0,0,0,1)
        )
        vector = (x, y, z, w, 1)
        x_out, y_out, z_out, w_out, _ = multiply_matrix_vector(matrix, vector)
        return (x_out, y_out, z_out, w_out)
    return new_function

def to_latex(m):
    pass