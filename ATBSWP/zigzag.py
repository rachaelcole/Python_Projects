# Simple zig zag text output animation

import time
import sys

indent = 0  # how many spaces to indent
indent_increasing = True    # Whether the indentation is increasing or not

try:
    while True:  # main program loop
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1)   # Pause for 0.1sec
        if indent_increasing:
            # Increase the number of spaces
            indent += 1
            if indent == 20:
                # Change direction
                indent_increasing = False
        else:
            # Decrease the number of spaces
            indent -= 1
            if indent == 0:
                # Change direction
                indent_increasing = True

except KeyboardInterrupt:
    sys.exit()
