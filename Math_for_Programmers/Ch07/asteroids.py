"""
asteroids.py - a demonstration of systems of linear equations: finding where lines, planes, etc., intersect

The player controls a spaceship (a triangle) and fires a laser at asteroids (polygons). The player must 
destroy the asteroids to prevent them from hitting and destroying the spaceship.

A key mechanic in this game is deciding whether the laser hits an asteroid. This requires us to determine whether
the line defining the laser beam intersects with the line segments outlining the asteroids. If these lines
intersect, the asteroid is destroyed.

This 2D example can be generalised to 3D and higher dimensions.
"""

import pygame
import vectors
from math import pi, sqrt, cos, sin, atan2
from random import randint, uniform
from linear_solver import do_segments_intersect
import sys


# DEFINE GAME OBJECTS:

class PolygonModel():
    def __init__(self, points):
        self.points = points
        self.rotation_angle = 0
        self.x = 0
        self.y = 0
        self.vx = 0
        self.vy = 0
        self.singular_velocity = 0

    def transformed(self):
        rotated = [vectors.rotate2d(self.rotation_angle, v) for v in self.points]
        return [vectors.add((self.x,self.y), v) for v in rotated]
    
    def move(self, milliseconds):
        dx, dy = self.vx * milliseconds / 1000.0, self.vy * milliseconds / 1000.0
        self.x, self.y = vectors.add((self.x, self.y), (dx, dy))
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
        # TODO: fix bug here, ship displays as one line rather than a triangular polygon
        super().__init__([(0,5,0), (-0.25,0.25), (-0.25,-0.25)])
    
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
        self.vx = 0  # == uniform(-1, 1)
        self.vy = 0  # == uniform(-1,1)
        self.angular_velocity = uniform(-pi/2, pi/2)


# RENDERING THE GAME:

# Initial game state
ship = Ship()
asteroid_count = 10
asteroids = [Asteroid() for _ in range(0,asteroid_count)]  # Creates a list of 10 asteroids
for ast in asteroids:  # Set the position of each object to a random point with coords from -10 to 10
    ast.x = randint(-9,9)
    ast.y = randint(-9,9)




# HELPERS / SETTINGS

# Colour RGBs
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
GREEN = (0,255,0)
RED = (255,0,0)

# Screen size for game in pixels:
width, height = 400, 400

# Define a to_pixels() function that maps an object from the centre of our coordinate system to the centre
# of a PyGame screen:
def to_pixels(x,y):
    return (width/2 + width * x / 20, height/2 - height * y / 20)

# Draws a polygon defined by points to the PyGame screen:
def draw_poly(screen, polygon_model, color=GREEN):
    pixel_points = [to_pixels(x,y) for x,y in polygon_model.transformed()]
    pygame.draw.aalines(screen, color, True, pixel_points, 10)

def draw_segment(screen, v1, v2, color=RED):
    pygame.draw.aaline(screen, color, to_pixels(*v1), to_pixels(*v2), 10)


# INITIALISE GAME ENGINE:
def main():
    pygame.init()
    screen = pygame.display.set_mode([width, height])
    pygame.display.set_caption('Asteroids!')
    done = False
    clock = pygame.time.Clock()

    while not done:
        clock.tick()
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop
        
        # UPDATE THE GAME STATE
        milliseconds = clock.get_time()
        keys = pygame.key.get_pressed()

        for ast in asteroids:
            ast.move(milliseconds)
        
        if keys[pygame.K_LEFT]:
            ship.rotation_angle += milliseconds * (2*pi / 1000)
        
        if keys[pygame.K_RIGHT]:
            ship.rotation_angle -= milliseconds * (2*pi / 1000)
        
        laser = ship.laser_segment()

        # DRAW THE SCENE
        screen.fill(WHITE)
        if keys[pygame.K_SPACE]:
            draw_segment(screen, *laser)
        
        draw_poly(screen, ship)

        for asteroid in asteroids:
            if keys[pygame.K_SPACE] and asteroid.does_intersect(laser):
                asteroids.remove(asteroid)
            else:
                draw_poly(screen, asteroid, color=GREEN)
        
        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    main()