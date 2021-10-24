#!/user/bin/env python3
# forestfiresim.py - A forest fires simulator demonstrating emergent behaviour

import random, sys, time
import bext

# Set up constants
WIDTH = 79
HEIGHT = 22
TREE = 'A'
FIRE = 'W'
EMPTY = ' '
INITIAL_TREE_DENSITY = 0.20
GROW_CHANCE = 0.01
FIRE_CHANCE = 0.01
PAUSE_LENGTH = 0.5


def create_new_forest():
    # Returns a dict for a new forest data structure
    forest = {'width': WIDTH, 'height': HEIGHT}
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if (random.random() * 100) <= INITIAL_TREE_DENSITY:
                forest[(x, y)] = TREE  # Start as a tree
            else:
                forest[(x, y)] = ' '  # Start as an empty space
    return forest


def display_forest(forest):
    # Displays the forest data structure on the screen
    bext.goto(0, 0)
    for y in range(forest['height']):
        for x in range(forest['width']):
            if forest[(x, y)] == TREE:
                bext.fg('green')
                print(TREE, end='')
            elif forest[(x, y)] == FIRE:
                bext.fg('red')
                print(FIRE, end='')
            elif forest[(x, y)] == EMPTY:
                print(EMPTY, end='')
        print()
    bext.fg('reset')  # Use the default font colour
    print(f'Grow chance: {GROW_CHANCE * 100}%   |   ', end='')
    print(f'Lightning chance: {FIRE_CHANCE * 100}%   |   ', end='')
    print('Press Ctrl-C to quit.')


def main():
    forest = create_new_forest()
    bext.clear()
    while True:  # Main program loop
        display_forest(forest)
        # Run a single simulation step
        next_forest = {'width': forest['width'], 'height': forest['height']}
        for x in range(forest['width']):
            for y in range(forest['height']):
                if (x, y) in next_forest:
                    continue    # If we've already set next_forest[(x, y)], do nothing here
                if (forest[(x, y)] == EMPTY) and (random.random() <= GROW_CHANCE):
                    # Grow a tree in this empty space
                    next_forest[(x, y)] = TREE
                elif (forest[(x, y)] == TREE) and (random.random() <= FIRE_CHANCE):
                    # Lightning sets this tree on fire
                    next_forest[(x, y)] = FIRE
                elif forest[(x, y)] == FIRE:
                    # This tree is currently burning
                    # Loop through all the neighbouring spaces
                    for ix in range (-1, 2):
                        for iy in range(-1, 2):
                            # Fire spreads to neighbouring trees
                            if forest.get((x + ix, y + iy)) == TREE:
                                next_forest[(x + ix, y + iy)] = FIRE
                    # The tree has burned down now, so erase it:
                    next_forest[(x, y)] = EMPTY
                else:
                    # Copy the existing object
                    next_forest[(x, y)] = forest[(x, y)]
        forest = next_forest
        time.sleep(PAUSE_LENGTH)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
