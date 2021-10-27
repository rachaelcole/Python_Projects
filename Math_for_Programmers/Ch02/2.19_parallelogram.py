from vectors import *
from vector_draw import *
from random import uniform

"""Suppose u = (-1, 1) and v = (1, 1), and s and r are real numbers where
-1 < r < 1 and -3 < s < 3. Where are the possible points on the plane where the 
vector r * u + s * v could end up?"""

u = (-1, 1)
v = (1, 1)

def random_r():
    return uniform(-3, 3)

def random_s():
    return uniform(-1, 1)

possibilities = [add(scale(random_r(), u), scale(random_s(), v)) for i in range(0, 500)]
print('Location of possible points for (r * u) + (s * v) given the constraints:')
draw(Points(*possibilities))