from vector_draw import *
from vectors import *
from transforms import *
from math import *
from draw3d import *

# Helper function to get the segments of the dinosaur polygon in 3D:
def polygon_segments_3d(points, color='blue'):
    count = len(points)
    return [Segment3D(points[i], points[(i+1) % count], color=color) for i in range(0, count)]

dino_vectors = [(6,4), (3,1), (1,2), (-1,5), (-2,5), (-3,4), (-4,4),
    (-5,3), (-5,2), (-2,2), (-5,1), (-4,0), (-2,1), (-1,0), (0,-3),
    (-1,-4), (1,-4), (2,-3), (1,-2), (3,-1), (5,1)
]
"""
The 2D dino:
draw(
    Points(*dino_vectors),
    Polygon(*dino_vectors)
)
"""
# 3D dino:
dino_vectors_3d = [(x,y,1) for x,y in dino_vectors]

draw3d(
    Points3D(*dino_vectors_3d, color='blue'),
    *polygon_segments_3d(dino_vectors_3d)
)

magic_matrix = (
    (1,0,3),
    (0,1,1),
    (0,0,1)
)

translated = [multiply_matrix_vector(magic_matrix, v) for v in dino_vectors_3d]

draw3d(
    Points3D(*dino_vectors_3d, color='C0'),
    *polygon_segments_3d(dino_vectors_3d, color='C0'),
    Points3D(*translated, color='C3'),
    *polygon_segments_3d(translated, color='C3')
)

translated_2d = [(x,y) for (x,y,z) in translated]

draw(
 
    Points(*translated_2d, color='C3'),
    Polygon(*translated_2d, color='C3')
)