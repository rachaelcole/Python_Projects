from math import sqrt, sin, cos, atan2, pi, acos

from numpy import tri

"""
We can combine vectors with operations to make new vectors, e.g.:
    def add(v1, v2):
        return (v1[0] + v2[0], v1[1] + v2[1])
"""

# def add(*vectors):
    # """Adding a vector translates existing point(s) """
    # return (sum([v[0] for v in vectors]), sum([v[1] for v in vectors]))

def add(*vectors):
    return tuple(map(sum, zip(*vectors)))

def subtract(v1, v2):
    return tuple(v1-v2 for (v1,v2) in zip(v1,v2))


def length(v):
    return sqrt(sum([coord ** 2 for coord in v]))

def dot(u, v):
    return sum([coord1 * coord2 for coord1, coord2 in zip(u,v)])

def distance(v1, v2):
    """Returns the length of the difference of two input vectors"""
    return length(subtract(v1, v2))

def perimeter(vectors):
    """Returns sum of distance of every pair of vectors in the list, and the first and last vectors"""
    distances = [distance(vectors[i], vectors[(i + 1) % len(vectors)]) for i in range(0, len(vectors))]
    return sum(distances)

def scale(scalar, v):
    """Multiplying a vector by a number is called scalar manipulation
    Ordinary numbers can be called scalars in this context
    Each component of a vector is scaled by the same factor as the scalar"""
    return tuple(scalar * coord for coord in v)

def to_cartesian(polar_vector):
    length, angle = polar_vector[0], polar_vector[1]
    return (length*cos(angle), length*sin(angle))

def rotate(angle, vectors):
    """Rotates Cartesian coordinates by a specified angle"""
    polars = [to_polar(v) for v in vectors]
    return [to_cartesian((l, a + angle)) for l, a in polars]

def translate(translation, vectors):
    """Takes a translation vector and a list of input vectors, and returns a list
    of all the input vectors translated by the translation vector by addition."""
    return [add(translation, v) for v in vectors]

def to_polar(vector):
    """Converts from cartesian to polar coordinates using atan2()."""
    x, y = vector[0], vector[1]
    angle = atan2(y, x)
    return (length(vector), angle)

def regular_polygon(n):
    """Returns Cartesian coordinates for the vertices of a regular n-sided polygon."""
    return [to_cartesian((1, 2 * pi * k / n)) for k in range(0, n)]

def angle_between(v1, v2):
    return acos(dot(v1,v2) / (length(v1) * length(v2)))

def cross(u, v):
    ux, uy, uz = u
    vx, vy, vz = v
    return(uy*vz - uz*vy, uz*vx - ux*vz, ux*vy - uy*vx)

def component(v, direction):
    return (dot(v, direction) / length(direction))

def unit(v):
    # Takes a vector and returns another in the same direction but with length 1
    return scale(1./length(v), v)

def vertices(faces):
    # Get the vertices from the faces
    return list(set([vertex for face in faces for vertex in face]))

def vector_to_2d(v):
    return (component(v, (1,0,0)), component(v, (0,1,0)))

def face_to_2d(face):
    return [vector_to_2d(vertex) for vertex in face]

def normal(face):
    # Takes a face and gives a vector perpendicular to it
    return(cross(subtract(face[1], face[0]), subtract(face[2], face[0])))

def split(face):
    midpoints = [unit(add(face[i], face[(i+1)%len(face)])) for i in range(0,len(face))]
    triangles = [(face[i], midpoints[i], midpoints[(i-1)%len(face)]) for i in range(0,len(face))]
    return [midpoints] + triangles

def rec_split(faces, depth=0):
    if depth == 0:
        return faces
    else:
        return rec_split([new_face for face in faces for new_face in split(face)], depth-1)