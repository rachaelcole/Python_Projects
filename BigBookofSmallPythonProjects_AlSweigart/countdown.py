#!/user/bin/env python3
# countdown.py - Shows a countdown timer animation using a seven-segment display

import sys
import time
import sevseg

seconds_left = 300  # Set to any number of seconds

try:
    while True:  # Main program loop
        # Clear the screen by printing several new lines
        print('\n' * 60)

        # Get the hours, mins, secs from seconds_left
        hours = str(seconds_left // 3600)
        mins = str(seconds_left // 60)
        secs = str(seconds_left % 60)
        """print("DEBUG: seconds are:", secs)
        print("DEBUG: minutes are:", mins)
        print("DEBUG: hours are:", hours)"""

        # Get the digit strings from the sevseg module
        h_digits = sevseg.get_sev_seg_str(hours, 2)
        h_toprow, h_middlerow, h_bottomrow = h_digits.splitlines()
        m_digits = sevseg.get_sev_seg_str(mins, 2)
        m_toprow, m_middlerow, m_bottomrow = m_digits.splitlines()
        s_digits = sevseg.get_sev_seg_str(secs, 2)
        s_toprow, s_middlerow, s_bottomrow = s_digits.splitlines()

        # Display the digits:
        print(h_toprow + '     ' + m_toprow + '     ' + s_toprow)
        print(h_middlerow + '  *  ' + m_middlerow + '  *  ' + s_middlerow)
        print(h_bottomrow + '  *  ' + m_bottomrow + '  *  ' + s_bottomrow)

        if seconds_left == 0:
            print()
            print('   * * * * BOOM * * * *')
            break

        print()
        print('Press Ctrl-C to quit.')

        time.sleep(1)  # Insert a one-second pause
        seconds_left -= 1
except KeyboardInterrupt:
    print('Bye!')
    sys.exit()
