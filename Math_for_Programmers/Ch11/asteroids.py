"""
asteroids.py - a demonstration of systems of linear equations: finding where lines, planes, etc., intersect

The player controls a spaceship (a triangle) and fires a laser at asteroids (polygons). The player must 
destroy the asteroids to prevent them from hitting and destroying the spaceship.

A key mechanic in this game is deciding whether the laser hits an asteroid. This requires us to determine whether
the line defining the laser beam intersects with the line segments outlining the asteroids. If these lines
intersect, the asteroid is destroyed.

This 2D example can be generalised to 3D and higher dimensions.

To implement motion, we'll consider the x- and y- coords of the asteroids as functions of time: x(t) and y(t).
The derivative of a position function with respect to time is velocity.
The derivative of velocity with respect to time is acceleration.
We can think of velocity and acceleration as vectors.

To move the asteroids, we will provide random, constant velocity functions, and integrate these functions in real time
to get the position of each asteroid in each frame using Euler's method.

We will also add user control to the spaceship, letting the spaceship accelerate in the direction it is pointed by the user.

We can model the gravitational force field of a black hole using a vector field. A vector field is an assignment of a vector
at every point in space. A gravitational field is a vector field telling us how strongly gravity pulls and in what 
direction from any given point.
"""

import pygame
from pygame import draw
import vectors
from math import pi, sqrt, cos, sin, atan2
from random import randint, uniform
from linear_solver import do_segments_intersect
import numpy as np
import sys


# DEFINE GAME OBJECTS:

bounce = True


class PolygonModel():
    def __init__(self, points):
        self.points = points
        self.rotation_angle = 0
        self.x = 0
        self.y = 0
        self.vx = 0
        self.vy = 0
        self.angular_velocity = 0
        self.draw_center = False

    def transformed(self):
        rotated = [vectors.rotate2d(self.rotation_angle, v) for v in self.points]
        return [vectors.add((self.x,self.y), v) for v in rotated]
    
    def move(self, milliseconds, thrust_vector=(0,0), gravity_sources=[]):
        ax, ay = thrust_vector
        gx, gy = gravitational_field(gravity_sources, self.x, self.y)
        ax += gx
        ay += gy
        self.vx += ax * milliseconds/1000
        self.vy += ay * milliseconds/1000

        dx, dy = self.vx * milliseconds / 1000.0, self.vy * milliseconds / 1000.0
        self.x, self.y = vectors.add((self.x, self.y), (dx,dy))
        if bounce:
            if self.x < -10 or self.x > 10:
                self.vx = - self.vx
            if self.y < -10 or self.y > 10:
                self.vy = - self.vy
        else:
            if self.x < -10:
                self.x += 20
            if self.y < -10:
                self.y += 20
            if self.x > 10:
                self.x -= 20
            if self.y > 10:
                self.y -= 20
        
        self.rotation_angle += self.angular_velocity * milliseconds / 1000.0
    
    def segments(self):
        point_count = len(self.points)
        points = self.transformed()
        return [(points[i], points[(i+1)%point_count]) for i in range(0,point_count)]
    
    def does_collide(self, other_poly):
        for other_segment in other_poly.segments():
            if self.does_intersect(other_segment):
                return True
        return False
    
    def does_intersect(self, other_segment):
        # Check whether the input segment intersects any segment of the given PolygonModel
        for segment in self.segments():
            if do_segments_intersect(other_segment,segment):
                return True
        return False


# The ship has a fixed triangular shape:
class Ship(PolygonModel):
    def __init__(self):
        super().__init__([(0.5,0), (-0.25,0.25), (-0.25,-0.25)])
    
    def laser_segment(self):
        dist = 20 * sqrt(2)  # Use Pythagorean theorem to find longest segment that fits on screen
        x,y = self.transformed()[0]  # Get value of first of the definition points (the tip of the ship)
        return (x,y), (x + dist * cos(self.rotation_angle), y + dist * sin(self.rotation_angle)) 


# The asteroid is between 5-9 vectors at equally spaced angles and random lengths between 0.5-1.0:
class Asteroid(PolygonModel):
    def __init__(self):
        # An asteroid has a random number of sides between 5 and 9
        sides = randint(5,9)  
        # Lengths are randomly selected between 0.5 and 1.0, and the angles are multiples of 2pi/n, where n = sides
        vs = [vectors.to_cartesian((uniform(0.5,1.0), 2*pi*i/sides)) for i in range(0,sides)]
        super().__init__(vs)
        self.vx = uniform(-1, 1)
        self.vy = uniform(-1,1)
        self.angular_velocity = uniform(-pi/2, pi/2)

# Asteroid helper function:
def trajectory(start,end,steps):
    xi, yi = start
    xf, yf = end
    xs = np.linspace(xi,xf,steps+1)
    ys = np.linspace(yi,yf,steps+1)
    model = Asteroid()
    asts = [Asteroid() for _ in range(0,steps+1)]
    for x,y,ast in zip(xs,ys,asts):
        ast.vx = ast.vy = ast.angular_velocity = 0
        ast.points = model.points
        ast.x = x
        ast.y = y
        ast.draw_center = True
    return asts


# Black hole class:
class BlackHole(PolygonModel):
    def __init__(self, gravity):
        vs = [vectors.to_cartesian((0.5, 2*pi*i/20)) for i in range(0,20)]
        super().__init__(vs)
        self.gravity = gravity



# RENDERING THE GAME:

# Initial game state
ship = Ship()
ship.x = 7
ship.y = 3

asteroid_count = 10
default_asteroids = [Asteroid() for _ in range(0,asteroid_count)]  # Creates a list of 10 asteroids

# Create a BlachHole object instance with gravity of 0.1
black_hole = BlackHole(0.1)
black_hole.x, black_hole.y = 0,0
black_holes = [black_hole]

# Multiply the vectors of the vector field by the gravity value to make the strength of
# the force field scale with the gravity of the black hole
def gravitational_field(sources, x, y):
    fields = [vectors.scale(- source.gravity, (x - source.x, y - source.y))
    for source in sources]
    return vectors.add(*fields)

for ast in default_asteroids:  # Set the position of each object to a random point with coords from -10 to 10
    ast.x = randint(-9,9)
    ast.y = randint(-9,9)


# HELPERS / SETTINGS

# Colour RGBs
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
GREEN = (0,255,0)
RED = (255,0,0)
LIGHT_GRAY = (240, 240, 240)
DARK_GRAY = (128, 128, 128)
# Screen size for game in pixels:
width, height = 400, 400

# Define a to_pixels() function that maps an object from the centre of our coordinate system to the centre
# of a PyGame screen:
def to_pixels(x,y):
    return (width/2 + width * x / 20, height/2 - height * y / 20)

# Draws a polygon defined by points to the PyGame screen:
def draw_poly(screen, polygon_model, color=BLACK, fill=False):
    pixel_points = [to_pixels(x,y) for x,y in polygon_model.transformed()]
    if fill:
        pygame.draw.polygon(screen, color, pixel_points, 0)
    else:
        pygame.draw.lines(screen, color, True, pixel_points, 2)
    if polygon_model.draw_center:
        cx, cy = to_pixels(polygon_model.x, polygon_model.y)
        pygame.draw.circle(screen, BLACK, (int(cx), int(cy)), 4, 4)

def draw_segment(screen, v1, v2, color=RED):
    pygame.draw.aaline(screen, color, to_pixels(*v1), to_pixels(*v2), 10)

def draw_grid(screen):
    for x in range(-9,10):
        draw_segment(screen, (x,-10), (x,10), color=LIGHT_GRAY)
    for y in range(-9,10):
        draw_segment(screen, (-10,y), (10,y), color=LIGHT_GRAY)
    draw_segment(screen, (-10,0), (10,0), color=DARK_GRAY)
    draw_segment(screen, (0,-10), (0,10), color=DARK_GRAY)





# INITIALISE GAME ENGINE:

# Set constants
thrust = 3
trajectory_mode = False
trajectory_frame = 1000

# Main game loop
def main():
    pygame.init()
    screen = pygame.display.set_mode([width, height])
    pygame.display.set_caption('Asteroids!')
    done = False
    clock = pygame.time.Clock()

    if trajectory_mode:
        screen.fill(WHITE)
        draw_grid(screen)
    
    since_last_trajectory_frame = trajectory_frame

    while not done:
        clock.tick()
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop
        
        # UPDATE THE GAME STATE
        milliseconds = clock.get_time()
        keys = pygame.key.get_pressed()

        for ast in default_asteroids:
            ast.move(milliseconds,(0,0),gravity_sources=black_holes)
        
        ship_thrust_vector = (0,0)
        
        if keys[pygame.K_LEFT]:
            ship.rotation_angle += milliseconds * (2*pi / 1000)
        
        if keys[pygame.K_RIGHT]:
            ship.rotation_angle -= milliseconds * (2*pi / 1000)
        
        # Detects if up arrow pressed
        if keys[pygame.K_UP]:
            ship_thrust_vector = vectors.to_cartesian((thrust, ship.rotation_angle))

        if keys[pygame.K_DOWN]:
            ship_thrust_vector = vectors.to_cartesian((- thrust, ship.rotation_angle))

        # Move the spaceship using updated velocities to update positions
        ship.move(milliseconds, ship_thrust_vector, black_holes)

        laser = ship.laser_segment()

        # DRAW THE SCENE

        if not trajectory_mode:
            screen.fill(WHITE)
            draw_grid(screen)

        if keys[pygame.K_SPACE]:
            draw_segment(screen, *laser)
        
        since_last_trajectory_frame += milliseconds
        if not trajectory_mode or since_last_trajectory_frame >= trajectory_frame:

            draw_poly(screen, ship)
            since_last_trajectory_frame = 0

            for bh in black_holes:
                draw_poly(screen, bh, fill=True)

            for asteroid in default_asteroids:
                if keys[pygame.K_SPACE] and asteroid.does_intersect(laser):
                    default_asteroids.remove(asteroid)
                else:
                    draw_poly(screen, asteroid, color=GREEN)
        
        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    main()