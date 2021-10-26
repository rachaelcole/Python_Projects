from vectors import *
from vector_draw import *

dino_vectors = [(6, 4), (3, 1), (1, 2), (-1, 5), (-2, 5), (-3, 4), (-4, 4), 
(-5, 3), (-5, 2), (-2, 2), (-5, 1), (-4, 0), (-2, 1), (-1, 0), (0, -3), 
(-1, -4), (1, -4), (2, -3), (1, -2), (3, -1), (5, 1)]

draw(Points(*dino_vectors), Polygon(*dino_vectors))

draw(Points(*[(x, x**2) for x in range(-10,11)]), grid=(1,10), nice_aspect_ratio=False)

# Translate the dino_vectors 1.5 units left and 2.5 units down:
dino_vectors2 = [add((-1.5, -2.5), v) for v in dino_vectors]
draw(Points(*dino_vectors, color=blue), 
Polygon(*dino_vectors, color=blue),
Points(*dino_vectors2, color=red),
Polygon(*dino_vectors2, color=red))

# Draw 100 dinos
def hundred_dinos():
    translations = [(12*x, 10*y) for x in range(-5, 5) for y in range(-5, 5)]
    dinos = [Polygon(*translate(t, dino_vectors), color=blue) for t in translations]
    draw(*dinos, grid=None, axes=None, origin=None)

hundred_dinos()

# Get the longest vector length in dino_vectors:
max(dino_vectors, key=length)