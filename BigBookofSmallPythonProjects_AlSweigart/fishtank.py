#!/user/bin/env python3
# fishtank.py - Displays a fishtank animation with wish, air bubblers, and kelp
# Requires bext. Must be run from command line/powershell

import random, sys, time, bext

# Initialise constants
WIDTH, HEIGHT = bext.size()
WIDTH -= 1
NUM_KELP = 2  # Try changing this
NUM_FISH = 10  # Try changing this
NUM_BUBBLERS = 1  # Try changing this
FRAMES_PER_SECOND = 4  # Try changing this
FISH_TYPES = [
    {'right': ['><>'], 'left':['<><']},
    {'right': ['>||>'], 'left':['<||<']},
    {'right': ['>))>'], 'left':['<[[<']},
    {'right': ['>||o', '>||.'], 'left': ['o||<', '.||<']},
    {'right': ['>))o', '>)).'], 'left': ['o[[<', '.[[<']},
    {'right': ['>-==>'], 'left': ['<==-<']},
    {'right': [r'>\\>'], 'left': ['<//<']},
    {'right': ['><)))*>'], 'left': ['<*(((><']},
    {'right': ['}-[[[*>'], 'left': ['<*]]]-{']},
    {'right': [']-<)))b>'], 'left': ['<d(((>-[']},
    {'right': ['><XXX*>'], 'left': ['<*XXX><']},
    {'right': ['_.-._.-^=>', '.-._.-.^=>', '-._.-._^=>', '._.-._.^=>'],
     'left': ['<=^-._.-._', '<=^.-._.-.', '<=^_.-._.-', '<=^._.-._.']},
]
LONGEST_FISH_LENGTH = 10  # Longest single string in FISH_TYPES
# The x and y positions where a fish runs into the edge of the screen
LEFT_EDGE = 0
RIGHT_EDGE = WIDTH - 1 - LONGEST_FISH_LENGTH
TOP_EDGE = 0
BOTTOM_EDGE = HEIGHT - 2


def getRandomColor():
    # Returns a string of a random colour
    return random.choice(('black', 'red', 'green', 'yellow', 'blue', 'purple', 'cyan', 'white'))


def generateFish():
    # Returns a dict that represents a fish
    fishType = random.choice(FISH_TYPES)
    # Set up colours for each character in the fish text
    colorPattern = random.choice(('random', 'head-tail', 'single'))
    fishLength = len(fishType['right'][0])
    if colorPattern == 'random':  # All parts are randomly coloured
        colors = []
        for i in range(fishLength):
            colors.append(getRandomColor())
    if colorPattern == 'single' or colorPattern == 'head-tail':
        colors = [getRandomColor()] * fishLength  # All the same colour
    if colorPattern == 'head-tail':  # Head/tail different from body
        headTailColor = getRandomColor()
        colors[0] = headTailColor  # Set head colour
        colors[-1] = headTailColor
    # Set up the rest of fish data structure:
    fish = {'right': fishType['right'],
            'left': fishType['left'],
            'colors': colors,
            'hSpeed': random.randint(1, 6),
            'vSpeed': random.randint(5, 15),
            'timeToHDirChange': random.randint(10, 60),
            'timeToVDirChange': random.randint(2, 20),
            'goingRight': random.choice([True, False]),
            'goingDown': random.choice([True, False])}
    # 'x' is always the leftmost side of the fish body:
    fish['x'] = random.randint(0, WIDTH - 1 - LONGEST_FISH_LENGTH)
    fish['y'] = random.randint(0, HEIGHT - 2)
    return fish


def simulateAquarium():
    # Simulate the movements in the aquarium for one Step
    global FISHES, BUBBLERS, BUBBLES, KELP, STEP
    # Simulate the fish:
    for fish in FISHES:
        # Move the fish horizontally
        if STEP % fish['hSpeed'] == 0:
            if fish['goingRight']:
                if fish['x'] != RIGHT_EDGE:
                    fish['x'] += 1  # Move the fish right
                else:
                    fish['goingRight'] = False  # Turn the fish around
                    fish['colors'].reverse()  # Turn the colours around
            else:
                if fish['x'] != LEFT_EDGE:
                    fish['x'] -= 1  # Move the fish left
                else:
                    fish['goingRight'] = True  # Turn the fish around
                    fish['colors'].reverse()
        # Fish can randomly change their hDir
        fish['timeToHDirChange'] -= 1
        if fish['timeToHDirChange'] == 0:
            fish['timeToHDirChange'] = random.randint(10, 60)
            # Turn the fish around:
            fish['goingRight'] = not fish['goingRight']
        # Move the fish vertically:
        if STEP % fish['vSpeed'] == 0:
            if fish['goingDown']:
                if fish['y'] != BOTTOM_EDGE:
                    fish['y'] += 1  # Move the fish down
                else:
                    fish['goingDown'] = False  # Turn the fish around
            else:
                if fish['y'] != TOP_EDGE:
                    fish['y'] -= 1  # Move the fish up
                else:
                    fish['goingDown'] = True
        fish['timeToVDirChange'] -= 1
        if fish['timeToVDirChange'] == 0:
            fish['timeToVDirChange'] = random.randint(2, 20)
            fish['goingDown'] = not fish['goingDown']
    for bubbler in BUBBLERS:
        if random.randint(1, 5) == 1:
            BUBBLES.append({'x': bubbler, 'y': HEIGHT - 2})
    for bubble in BUBBLES:
        diceRoll = random.randint(1, 6)
        if (diceRoll == 1) and (bubble['x'] != LEFT_EDGE):
            bubble['x'] -= 1
        elif (diceRoll == 2) and (bubble['x'] != RIGHT_EDGE):
            bubble['x'] += 1
        bubble['y'] -= 1
    for i in range(len(BUBBLES) - 1, -1, -1):
        if BUBBLES[i]['y'] == TOP_EDGE:
            del BUBBLES[i]
    for kelp in KELPS:
        for i, kelpSegment in enumerate(kelp['segments']):
            if random.randint(1, 20) == 1:
                if kelpSegment == '(':
                    kelp['segments'][i] = ')'
                elif kelpSegment == ')':
                    kelp['segments'][i] = '('


def drawAquarium():
    # Draw the aquarium on the screen
    global FISHES, BUBBLERS, BUBBLES, KELP, STEP
    # Draw quit message
    bext.fg('white')
    bext.goto(0, 0)
    print('Fish Tank\nCtrl-C to quit')
    # Draw the bubbles
    bext.fg('white')
    for bubble in BUBBLES:
        bext.goto(bubble['x'], bubble['y'])
        print(random.choice(('o', 'O')), end='')
    # Draw the fish
    for fish in FISHES:
        bext.goto(fish['x'], fish['y'])
        # Get the correct right- or left-facing fish text
        if fish['goingRight']:
            fishText = fish['right'][STEP % len(fish['right'])]
        else:
            fishText = fish['left'][STEP % len(fish['left'])]
        # Draw each char of the fish text in the right colour
        for i, fishPart in enumerate(fishText):
            bext.fg(fish['colors'][i])
            print(fishPart, end='')
    # Draw the kelp
    bext.fg('green')
    for kelp in KELPS:
        for i, kelpSegment in enumerate(kelp['segments']):
            if kelpSegment == '(':
                bext.goto(kelp['x'], BOTTOM_EDGE - i)
            elif kelpSegment == ')':
                bext.goto(kelp['x'] + 1, BOTTOM_EDGE - i )
            print(kelpSegment, end='')
    # Draw the sand at the bottom
    bext.fg('yellow')
    bext.goto(0, HEIGHT - 1)
    print(chr(9617) * (WIDTH - 1), end='')
    sys.stdout.flush()


def clearAquarium():
    # Draws empty spaces over everything on the screen
    global FISHES, BUBBLERS, BUBBLES, KELP
    # Draw the bubbles
    for bubble in BUBBLES:
        bext.goto(bubble['x'], bubble['y'])
        print(' ', end='')
    # Draw the fish
    for fish in FISHES:
        bext.goto(fish['x'], fish['y'])
        # Draw each char of the fish text in the right colour
        print(' ' * len(fish['left'][0]), end='')
    # Draw the kelp
    for kelp in KELPS:
        for i, kelpSegment in enumerate(kelp['segments']):
            bext.goto(kelp['x'], HEIGHT - 2 - i)
            print('  ', end='')
    sys.stdout.flush()


def main():
    global FISHES, BUBBLERS, BUBBLES, KELPS, STEP
    bext.bg('black')
    bext.clear()

    # Generate global vars
    FISHES = []
    for i in range(NUM_FISH):
        FISHES.append(generateFish())

    # Bubbles are drawn, but not the bubblers
    BUBBLERS = []
    for i in range(NUM_BUBBLERS):
        # Each bubbler starts at a random position
        BUBBLERS.append(random.randint(LEFT_EDGE, RIGHT_EDGE))
    BUBBLES = []

    KELPS = []
    for i in range(NUM_KELP):
        kelpx = random.randint(LEFT_EDGE, RIGHT_EDGE)
        kelp = {'x': kelpx, 'segments': []}
        # Generate each segment of the kelp
        for i in range(random.randint(6, HEIGHT - 1)):
            kelp['segments'].append(random.choice(['(', ')']))
        KELPS.append(kelp)

    # Run the simulation
    STEP = 1
    while True:
        simulateAquarium()
        drawAquarium()
        time.sleep(1 / FRAMES_PER_SECOND)
        clearAquarium()
        STEP += 1


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
