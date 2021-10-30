from math import *
from random import randint
import numpy as np
import matplotlib.pyplot as plt
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

def rotate2d(angle, vector):
    """Rotates Cartesian coordinates by a specified angle"""
    l, a = to_polar(vector)
    return to_cartesian((l, a + angle))

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

def linear_combination(scalars, *vectors):
    scaled = [scale(s,v) for s,v in zip(scalars, vectors)]
    return add(*scaled)

def stretch_X(vector):
    x,y,z = vector
    return(4.*x, y, z)

def stretch_y(vector):
    x, y, z = vector
    return(x, 4.*y, z)

def cube_stretch_x(vector):
    x, y, z = vector
    return (x, y*y*y, z)

def slant_xy(vector):
    x,y,z = vector
    return(x+y, y, z)

# Generic average function that can be used on any type of vector:
def average(v1, v2):
    return 0.5 * v1 + 0.5 * v2

# Plotting function that draws the graph of one or more functions on a specified range of inputs
def plot(fs, xmin, xmax):
    xs = np.linspace(xmin,xmax,100)
    fig, ax = plt.subplots()
    ax.axhline(y=0, color='k')
    ax.axvline(x=0, color='k')
    for f in fs:
        ys = [f(x) for x in xs]
        plt.plot(xs, ys)

# Takes three 3D points as inputs and returns the standard for equation of the plane they lie in:
def plane_equation(p1,p2,p3):
    parallel1 = subtract(p2,p1)
    parallel2 = subtract(p3,p1)
    a,b,c = cross(parallel1, parallel2)
    d = dot((a,b,c), p1)
    return a,b,c,d


# A function that carries out Euler's method automatically for a constantly accelerating
# object (n.b., under-approximates the y-axes):
def eulers_method(s0,v0,a,total_time,step_count):
    trajectory = [s0]
    s = s0
    v = v0
    dt = total_time / step_count
    for _ in range(0, step_count):
        s = add(s,scale(dt,v))
        v = add(v,scale(dt,a))
        trajectory.append(s)
    return trajectory


# Over-approximate the y-axes:
def eulers_method_overapprox(s0,v0,a,total_time,step_count):
    trajectory = [s0]
    s = s0
    v = v0
    dt = total_time / step_count
    for _ in range(0, step_count):
        v = add(v,scale(dt,a))
        s = add(s,scale(dt,v))
        trajectory.append(s)
    return trajectory
