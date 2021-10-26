from math import sqrt, sin, cos, atan2
# We can combine vectors with operations to make new vectors, e.g.:
# def add(v1, v2):
#    return (v1[0] + v2[0], v1[1] + v2[1])

def add(*vectors):
    # Adding a vector translates existing point(s) 
    return (sum([v[0] for v in vectors]), sum([v[1] for v in vectors]))

def subtract(v1, v2):
    return (v1[0] - v2[0], v1[1] - v2[1])


def length(v):
    # The length of a vector (x, y) is the square root of x**2 + y**2
    return sqrt(v[0]**2 + v[1]**2)

def distance(v1, v2):
    return length(subtract(v1, v2))

def perimeter(vectors):
    distances = [distance(vectors[i], vectors[(i + 1) % len(vectors)]) for i in range(0, len(vectors))]
    return sum(distances)

def scale(scalar, v):
    # Multiplying a vector by a number is called scalar manipulation
    # Ordinary numbers can be called scalars in this context
    # Each component of a vector is scaled by the same factor as the scalar
    return (scalar * v[0], scalar * v[1])

def to_cartesian(polar_vector):
    length, angle = polar_vector[0], polar_vector[1]
    return (length*cos(angle), length*sin(angle))

def rotate(angle, vectors):
    polars = [to_polar(v) for v in vectors]
    return [to_cartesian((l, a + angle)) for l, a in polars]

def translate(translation, vectors):
    # Takes a translation vector and a list of input vectors, and returns a list
    # of all the input vectors translated by the translation vector by addition
    return [add(translation, v) for v in vectors]

def to_polar(vector):
    x, y = vector[0], vector[1]
    angle = atan2(y, x)
    return (length(vector), angle)