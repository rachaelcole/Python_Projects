#! user/bin/env/python3
# conwaysgameoflife.py - Conway's Game of Life cellular automata simulation

import copy
import random
import sys
import time

# cell grid dimensions
width = 79
height = 20

alive = 'O'  # try changing this
dead = ' '  # try changing this

# The cells and next_cells are dicts for the state of the game. Their keys are (x, y) tuples and their values are one
# of the alive or dead values
next_cells = {}

# Put random dead and alive cells into next_cells
for x in range(width):  # Loop over every possible column
    for y in range(height):  # Loop over every possible row
        # 50/50 chance for starting cells to be alive or dead
        if random.randint(0, 1) == 0:
            next_cells[(x, y)] = alive  # add a living cell
        else:
            next_cells[(x, y)] = dead  # add a dead cell

while True:  # Main game loop
    # Each iteration of this loop is a step of the simulation
    print('\n' * 50)  # Separate each step with new lines
    cells = copy.deepcopy(next_cells)

    # Print cells on the screen
    for y in range(height):
        for x in range(width):
            print(cells[(x, y)], end='')  # Print the O or space
        print()  # Print a new line at the end of the row
    print('Press Ctrl-C to quit.')

    # Calculate the next step's cells based on the current step's cells:
    for x in range(width):
        for y in range(height):
            # Get the neighbouring coords of (x, y)
            left = (x - 1) % width
            right = (x + 1) % width
            above = (y - 1) % height
            below = (y + 1) % height

            # Count num of living neighbours
            num_neighbours = 0
            if cells[(left, above)] == alive:
                num_neighbours += 1  # Top-left neighbour is alive
            if cells[(x, above)] == alive:
                num_neighbours += 1  # Top neighbour is alive
            if cells[(right, above)] == alive:
                num_neighbours += 1  # Top-right neighbour is alive
            if cells[(left, y)] == alive:
                num_neighbours += 1  # Left neighbour is alive
            if cells[(right, y)] == alive:
                num_neighbours += 1  # Right neighbour is alive
            if cells[(left, below)] == alive:
                num_neighbours += 1  # Bottom-left neighbour is alive
            if cells[(x, below)] == alive:
                num_neighbours += 1  # Bottom neighbour is alive
            if cells[(right, below)] == alive:
                num_neighbours += 1  # Bottom-right neighbour is alive

            # Set cells based on Conway's Game of Life rules:
            if cells[(x, y)] == alive and (num_neighbours == 2 or num_neighbours == 3):
                # Living cells with 2 or 3 neighbours stay alive
                next_cells[(x, y)] = alive
            elif cells[(x, y)] == dead and num_neighbours == 3:
                # Dead cells with 3 neighbours become alive
                next_cells[(x, y)] = alive
            else:
                # Everything else dies, or stays dead
                next_cells[(x, y)] = dead

    try:
        time.sleep(1)  # Add a 1-sec pause to reduce flickering
    except KeyboardInterrupt:
        print("Conway's Game of Life")
        sys.exit()  # When Ctrl-C is pressed, quit
