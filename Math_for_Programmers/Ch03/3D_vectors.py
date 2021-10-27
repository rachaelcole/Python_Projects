from vectors import *
from draw2d import *
from draw3d import *
from matplotlib.cm import get_cmap


"""
3D VECTORS

In 3D, we have (x, y, z) co-ordinates representing height, width, and depth.

"""


print("Drawing the points (2,2,2) and (1,-2,-2):")
# draw3d(Points3D((2,2,2),(1,-2,-2)))

draw3d(
    Points3D((2,2,2),(1,-2,-2)),
    Segment3D((2,2,2),(1,-2,-2)),
    Box3D(2,2,2),
    Box3D(1,-2,-2)
)


""" Rendering a 3D object in 2D """
# Define the octahedron's vectors by the coords (1,0,0), (0,1,0), (0,0,1) and their opposites:
octahedron = [
    [(1,0,0), (0,1,0), (0,0,1)],
    [(1,0,0), (0,0,-1), (0,1,0)],
    [(1,0,0), (0,0,1), (0,-1,0)],
    [(1,0,0), (0,-1,0), (0,0,-1)],
    [(-1,0,0), (0,0,1), (0,1,0)],
    [(-1,0,0), (0,1,0), (0,0,-1)],
    [(-1,0,0), (0,-1,0), (0,0,1)],
    [(-1,0,0), (0,0,-1), (0,-1,0)],

]

import matplotlib.cm



blues = matplotlib.cm.get_cmap('Blues')




def render(faces, light=(1,2,3), color_map=blues, lines=None):
    polygons = []
    for face in faces:
        unit_normal = unit(normal(face))  # For each face, compute a vector of length 1 perpendicular to it
        if unit_normal[2] > 0:  # Only proceeds if z is positive (i.e., it points toward the viewer)
            c = color_map(1 - dot(unit(normal(face)), unit(light)))  # The larger the dot, the less shading
            p = Polygon2D(*face_to_2d(face), fill=c, color=lines)  # Reveal skeleton with lines
            polygons.append(p)
    draw2d(*polygons, axes=False, origin=False, grid=None)

render(octahedron, color_map=blues, lines=black)



def split(face):
    midpoints = [unit(add(face[i], face[(i+1)%len(face)])) for i in range(0,len(face))]
    triangles = [(face[i], midpoints[i], midpoints[(i-1)%len(face)]) for i in range(0,len(face))]
    return [midpoints] + triangles

def rec_split(faces, depth=0):
    if depth == 0:
        return faces
    else:
        return rec_split([new_face for face in faces for new_face in split(face)], depth-1)

def sphere_approx(n):
    return rec_split(octahedron, n)

render(sphere_approx(3), lines='k')