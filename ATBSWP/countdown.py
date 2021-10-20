#! python3
# countdown.py - Counts down from 60 and plays a sound file (alarm.wav) when the counter == 0

import time
import subprocess

time_left = 60

# Countdown
while time_left > 0:
    print(time_left)
    time.sleep(1)
    time_left = time_left - 1

# Play sound file
subprocess.Popen(['start', 'alarm.wav'], shell=True)
