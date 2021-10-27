
from teapot import load_triangles
from draw_model import draw_model
from transforms import *
import camera
from vectors import *
from math import *
import sys
from math import sin,cos

def get_rotation_matrix(t): #1
    seconds = t/1000 #2
    return (
        (cos(seconds),0,-sin(seconds)),
        (0,1,0),
        (sin(seconds),0,cos(seconds))
    )

if '--snapshot' in sys.argv:
    camera.default_camera = camera.Camera('fig_4.4_draw_teapot',[0])


draw_model(load_triangles(), get_matrix=get_rotation_matrix)


