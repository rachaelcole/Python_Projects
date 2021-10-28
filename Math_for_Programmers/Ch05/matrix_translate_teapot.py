from teapot import load_triangles
from draw_model import draw_model
from transforms import polygon_map
from vectors import *

"""
In 4D space, we often represent the fourth dimension as 'time', or 'spacetime'.
The origin of the spacetime is the origin of the space at the moment when time, t, is
equal to zero.

A 4D vector can be represented as a four-tuple of numbers.
"""
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


# Draw the teapot translated by (2, 2, -3):
draw_model(polygon_map(translate_3d((2,2,-3)), load_triangles()))

# 4D vector x 4D vector:
print(translate_4d((1,2,3,4))((10,20,30,40)))