# Conway's Game of Life
import random
import time
import copy

WIDTH = 20
HEIGHT = 5

# Create a list of lists for the cells
nextCells = []
for x in range(WIDTH):
    column = []                                     # Create a new column
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            column.append('#')                      # Add a living cell
        else:
            column.append(' ')                      # Add a dead cell
    nextCells.append(column)                        # NextCells is a list of column lists

while True:                                         # main program loop
    print('\n\n\n\n\n\n')                           # separate each step with new lines
    currentCells = copy.deepcopy(nextCells)

    # Print currentCells on the screen:
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end='')       # Print the # or space
        print()                                     # Print a new line at the end of the row

    # Calculate the next step's cells based on current step's cells
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # Get neighbouring coordinates
            # '%WIDTH' ensures leftCoord is always between 0 and WIDTH - 1
            leftCoord = (x - 1) % WIDTH
            rightCoord = (x + 1) % WIDTH
            aboveCoord = (y - 1) % HEIGHT
            belowCoord = (y + 1)  % HEIGHT

            # Count number of living neighbours
            numNeighbours = 0
            if currentCells[leftCoord][aboveCoord] == '#':
                numNeighbours += 1                  # top-left neighbour is alive
            if currentCells[x][aboveCoord] == '#':
                numNeighbours += 1                  # top neighbour
            if currentCells[rightCoord][aboveCoord] == '#':
                numNeighbours += 1                  # top-right neighbour
            if currentCells[leftCoord][y] == '#':
                numNeighbours += 1                  # left neighbour
            if currentCells[rightCoord][y] == '#':
                numNeighbours += 1                  # right neighbour
            if currentCells[leftCoord][belowCoord] == '#':
                numNeighbours += 1                  # bottom left neighbour
            if currentCells[x][belowCoord] == '#':
                numNeighbours += 1                  # bottom neighbour
            if currentCells[rightCoord][belowCoord] == '#':
                numNeighbours += 1                  # bottom-right neighbour

            # Set cell based on Conway's Game of Life rules
            if currentCells[x][y] == '#' and (numNeighbours == 2 or numNeighbours == 3):
                # Living cells with 2 or 3 neighbours stay alive
                nextCells[x][y] = '#'
            elif currentCells[x][y] == ' ' and numNeighbours == 3:
                # Dead cells with 3 neighbours become alive
                nextCells[x][y] = '#'
            else:
                # Everything else dies or stays dead
                nextCells[x][y] = ' '
    time.sleep(1)
