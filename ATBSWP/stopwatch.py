#! python3
# stopwatch.py - Track time elapsed between presses of Enter key, track laps and print to command line

import time

# Display program instructions
print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch. Press Ctrl-Z to quit.')
input()
print('Started.')
start_time = time.time()  # Get first lap's start time
last_time = start_time
lap_num = 1

# Start tracking the lap times
try:
    while True:
        input()
        lap_time = round(time.time() - last_time, 2)
        total_time = round(time.time() - start_time, 2)
        response = f'Lap #{lap_num}: {total_time}s ({lap_time}s)'
        print((response.ljust(40 - len(response))).rjust(15))
        lap_num += 1
        last_time = time.time()  # Reset the last lap time
except KeyboardInterrupt:
    # Handle the Ctrl-Z exception to keep its error message from displaying
    print('\nDone.')
