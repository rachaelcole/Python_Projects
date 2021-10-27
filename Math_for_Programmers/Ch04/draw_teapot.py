
from teapot import load_triangles
from draw_model import draw_model
from transforms import *
import camera
from vectors import *
from math import *
import sys
 
if '--snapshot' in sys.argv:
    camera.default_camera = camera.Camera('fig_4.4_draw_teapot',[0])

original_triangles = load_triangles()

# Original teapot
# draw_model(original_triangles)

# scale2() multiplies an inbut vector by scalar 2:
def scale2(v):
    return scale(2.0, v)

scaled_triangles = [
    [scale2(vertex) for vertex in triangle] for triangle in original_triangles
]

draw_model(scaled_triangles)

def translate1left(v):
    return add((-1,0,0), v)

translated_triangles = [[translate1left(scale2(vertex)) for vertex in triangle] for triangle in original_triangles]

draw_model(translated_triangles)

draw_model(polygon_map(rotate_x_by(pi/2.), load_triangles()))


draw_model(polygon_map(stretch_X, load_triangles()))



