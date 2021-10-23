#!/user/bin/env python3
# bitmapmessage.py - Displays a text message according to the provided bitmap image
# bitmap image from https://inventwithpython.com/bitmapworld.txt

import sys

# (!) Try changing this multiline string to other images:
bitmap = """
....................................................................
   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** ************** *
           *********            *******   **************** * *
            ********           ***************************  *
   *        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 ******         *************    **   **  *
                 ********        *************    *  ** ***
                   ********         ********          * *** ****
                   *********         ******  *        **** ** * **
                   *********         ****** * *           *** *   *
                     ******          ***** **             *****   *
                     *****            **** *            ********
                    *****             ****              *********
                    ****              **                 *******   *
                    ***                                       *    *
                    **     *                    *
....................................................................
"""

print('Bitmap Message')
print('Enter the message to display with the bitmap:')
message = input('> ')
if message == '':
    sys.exit()

# Loop over each line in the bitmap
for line in bitmap.splitlines():  # returns a list of strings, each string is a line in the multiline bitmap string
    # Loop over each character in the line:
    for i, bit in enumerate(line):
        if bit == ' ':
            # Print an empty space
            print(' ', end='')
        else:
            # Print a character from the message
            print(message[i % len(message)], end='')  # Repeats the characters in message as i increases
    print()  # Print a new line
