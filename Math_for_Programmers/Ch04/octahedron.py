import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import matplotlib.cm
from vectors import *
from math import *

def normal(face):
    return(cross(subtract(face[1], face[0]), subtract(face[2], face[0])))

blues = matplotlib.cm.get_cmap('Blues')

def shade(face, color_map=blues, light=(1,2,3)):
    return color_map(1 - dot(unit(normal(face)), unit(light)))

light = (1, 2, 3)

faces = [[(1,0,0), (0,1,0), (0,0,1)],
    [(1,0,0), (0,0,-1), (0,1,0)],
    [(1,0,0), (0,0,1), (0,-1,0)],
    [(1,0,0), (0,-1,0), (0,0,-1)],
    [(-1,0,0), (0,0,1), (0,1,0)],
    [(-1,0,0), (0,1,0), (0,0,-1)],
    [(-1,0,0), (0,-1,0), (0,0,1)],
    [(-1,0,0), (0,0,-1), (0,-1,0)],]

def Axes():
    axes = [
        [(-1000,0,0),(1000,0,0)],
        [(0,-1000,0),(0,1000,0)],
        [(0,0,-1000),(0,0,1000)]
    ]
    glBegin(GL_LINES)
    for axis in axes:
        for vertex in axis:
            glColor3fv((1,1,1))
            glVertex3fv(vertex)
    glEnd()

pygame.init()
display = (400,400)  # 400x400px window
window = pygame.display.set_mode(display, DOUBLEBUF|OPENGL)  # OpenGL for graphics and double-buffering

gluPerspective(45, 1, 0.1, 50.0) # Describes our perspective looking at the scene
glTranslatef(0.0,0.0,-5)  # We will observe from 5 units up
glEnable(GL_CULL_FACE)
glEnable(GL_DEPTH_TEST)
glCullFace(GL_BACK)

clock = pygame.time.Clock()  # Initialise a clock to measure time in game
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Check if user has quit/closed window
            pygame.quit()
            quit()

    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    """
    Just as glTranslatef() tells OpenGL the position from which we want to see the 3D scene we're rendering,
    the glRotatef() function lets us change the angle at which we are viewing the scene.
    glRotatef(theta, x, y, z) rotates the scene by the angle theta about an axis specified by the vector (x,y,z).
    For example:
        glRotatef(30,0,0,1) rotates the scene 30 degrees about the z-axis
        glRotatef(30,0,1,1) rotates the scene 30 degrees about the axis (0,1,1), which is 45 degrees between the y- and z- axes

    To animate the rotation, we can call glRotatef with a small angle in every frame. We add glRotatef(1,1,1,1) within the infinite while loop
    before glBegin() to cause the octahedron to rotate by 1 degree per frame about an axis in the direction (1,1,1).

    We can calculate the degrees per millisecond to guarantee the scene rotates 360 degrees every 5 seconds        
    """
    degrees_per_second = 360./5.
    degrees_per_millisecond = degrees_per_second / 1000
    milliseconds = clock.tick()
    degrees = degrees_per_millisecond * milliseconds
    glRotatef(degrees,1,1,1)

    glBegin(GL_TRIANGLES) # We are about to draw triangles
    
    for face in faces:
        color = shade(face,blues,light)
        for vertex in face:  # Set colour based on shading of vertex
            glColor3fv((color[0], color[1], color[2]))
            glVertex3fv(vertex)
    glEnd()
    pygame.display.flip()
