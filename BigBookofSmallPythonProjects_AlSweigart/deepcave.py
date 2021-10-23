#! user/bin/env/python3
# deepcave.py - An endless cave-walking animation

import random, sys, time

# Set up constants
width = 70
pause_amount = 0.05

print('Deep Cave')
print('Press Ctril-C to stop.')

time.sleep(2)

left_width = 20
gap_width = 10

while True:
    # Display tunnel segment
    right_width = width - gap_width - left_width
    print(('#' * left_width) + (' ' * gap_width) + ('#' * right_width))
    # Check for Ctrl-C during the brief pause
    try:
        time.sleep(pause_amount)
    except KeyboardInterrupt:
        sys.exit()
    # Adjust left side width
    dice_roll = random.randint(1, 6)
    if dice_roll == 1 and left_width > 1:
        left_width = left_width - 1  # Decrease left side width
    elif dice_roll == 2 and left_width + gap_width < width - 1:
        left_width = left_width + 1  # Increase left side width
    else:
        pass
    # Adjust the gap width
    dice_roll = random.randint(1, 6)
    if dice_roll == 1 and gap_width > 1:
        gap_width = gap_width - 1  # Decrease the gap width
    elif dice_roll == 2 and left_width + gap_width < width - 1:
        gap_width = gap_width + 1  # Increase gap width
    else:
        pass
