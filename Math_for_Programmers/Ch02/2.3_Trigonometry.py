from math import degrees, tan, sin, cos, pi, atan2
from vector_draw import *
from vectors import *
from dino_vectors import dino_vectors

"""
TRIGONOMETRY

Cartesian co-ordinates are the usual (x, y) positions on a plane.
Polar co-ordinates give the length and angle of a vector as (length, angle in degrees), e.g.,
(5, 37°).

Cartesian co-ordinates are useful for adding/subtracting vectors.
Polar co-ordinates are useful for rotating vectors, for example.

Every angle gives a constant ratio: 
    - 116.57° has a ratio of -2
    - 45° has a ratio of 1
    - -200° has a ratio of 0.36

Given an angle, the coordinates of vectors along that angle will have a constant ratio.
This is called the tanget of the angle. The tangent function is tan().

If we measure some distance at some angle, the tangent of the angle gives us the vertical
distance covered divided by the horizontal distance.

Sine (sin) and cosine (cos) help us find the co-ordinates of an angle. They give the vertical
and horizontal distance covered relative to the overall distance.

sin(angle) = vertical/distance
cos(angle) = horizontal/distance

If you know: 
    - the sine and cosine of an angle θ, and 
    - a distance r traveled in that direction, 
the Cartesian coordinates are given by (r * cos(θ), r * sin(θ)).

"""

# Tangent function gives ratio of coordinates of vectors along an angle
x= tan(45)  # Returns answer in radians, i.e, 1.61977519...etc
print(x)
# 1 radian = 57.296 degrees
# pi*radians = 180 degrees
# 2*pi*radians = 360 degrees
# pi / 4 * radians = 45 degrees
x = tan(pi/4)
print(x)  # Returns the tangent of the angle 45 degrees, 0.999999999, i.e., 1


def to_cartesian(polar_vector):
    """Takes a pair of polar coordinates and returns their Cartesian coordinates."""
    length, angle = polar_vector[0], polar_vector[1]
    return (length * cos(angle), length * sin(angle))

# 5 units at an angle of 37 degrees converted to Cartesian coords:
angle = 37 * pi / 180
print(to_cartesian((5, angle)))  # Returns (3.99, 3.00): round to (4, 3)


def to_polar(vector):
    """Converts from cartesian to polar coordinates using atan2()."""
    x, y = vector[0], vector[1]
    angle = atan2(y, x)
    return (length(vector), angle)

# Confirm that the vector given by Cartesian coords (-1.34, 2.68) has a length of
# approximately 3:
print(length((-1.34, 2.68)))

polar_coords = [(cos(5*x*pi/500.0), 2*pi*x/1000.0) for x in range(0, 1000)]
vectors = [to_cartesian(p) for p in polar_coords]
draw(Polygon(*vectors, color=green))


"""
2.4 Transforming collections of vectors

Adding to the angle of a polar coordinate rotates a vector counterclockwise.
Subtracting from the angle of a polar coordinate rotates the vector clockwise.

"""

rotation_angle = pi / 4
dino_polar = [to_polar(v) for v in dino_vectors]
dino_rotated_polar = [(l, angle + rotation_angle) for l, angle in dino_polar]
dino_rotated = [to_cartesian(p) for p in dino_rotated_polar]
draw(
    Polygon(*dino_vectors, color=gray),
    Polygon(*dino_rotated, color=red)
)

new_dino = translate((8, 8), rotate(5 * pi / 3, dino_vectors))
draw(
    Polygon(*dino_vectors, color=gray),
    Polygon(*new_dino, color=red)
)

polygon = regular_polygon(7)
draw(Polygon(*polygon, color=blue))