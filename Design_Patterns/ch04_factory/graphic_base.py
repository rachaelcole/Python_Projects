# Creating factory classes using PyGame
# Factory classes degine objects that take a certain set of parameters and use that to create objects of some other class
# Abstract factory classes serve as the template to build these factory classes

import pygame

window_dimensions = 800, 600
screen = pygame.display.set_mode(window_dimensions) # Sets a 400x300px screen

x = 100
y = 100

player_quits = False

while not player_quits:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            player_quits = True
        
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: y -=4
        if pressed[pygame.K_DOWN]: y += 4
        if pressed[pygame.K_LEFT]: x -= 4
        if pressed[pygame.K_RIGHT]: x += 4

        screen.fill((0,0,0))
        pygame.draw.rect(screen, (255, 255, 0), pygame.Rect(x, y, 20, 20))

    pygame.display.flip()  # Update the display

# Reference: 
# Badenhurst, Wessel. "Chapter 4: Factory Pattern". Practical Python Design Patterns: Pythonic Solutions to Common Problems, Apress, October 20, 2017, pp. 61-73,
# DOI: https://doi.org/10.1007/978-1-4842-2680-3_4. 