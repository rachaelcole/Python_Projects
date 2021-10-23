#!/user/bin/env python3
# digitalstream.py - Displays a 'binary rain' animation on the terminal window
import random, shutil, time, sys

# Set up constants
MIN_STREAM_LENGTH = 6                   # Try changing to 1 or 50
MAX_STREAM_LENGTH = 14                  # Try changing to 100
PAUSE = 0.1                             # Try changing to 0.0 or 2.0
STREAM_CHARS = ['0', '1']               # Try changing to other chars
DENSITY = 0.1                           # Density can range from 0.0 to 1.0
WIDTH = shutil.get_terminal_size()[0]   # Get the size of the terminal window
WIDTH -= 1                              # We can't print the last column on Windows without it adding a new line
                                        # automatically, so we reduce the WIDTH by 1 to compensate
print('Digital Stream')
print('Press Ctrl-C to quit.')
time.sleep(2)

try:
    # For each column, when the counter is 0, no stream is shown. Otherwise, it acts as a counter for how many times a
    # 1 or 0 should be displayed in that column.
    columns = [0] * WIDTH
    while True:
        # Set up the counter for each column:
        for i in range(WIDTH):
            if columns[i] == 0:
                if random.random() <= DENSITY:
                    # Restart a stream on this column
                    columns[i] = random.randint(MIN_STREAM_LENGTH, MAX_STREAM_LENGTH)
            # Display an empty space or a 1/0 character
            if columns[i] > 0:
                print(random.choice(STREAM_CHARS), end='')
                columns[i] -= 1
            else:
                print(' ', end='')
        print()  # Print new line at the end of the row of columns
        sys.stdout.flush()  # Ensure text appears on the screen
        time.sleep(PAUSE)
except KeyboardInterrupt:
    sys.exit()
