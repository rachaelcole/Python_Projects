#! python3
# map_it.py - Takes a street address from the command line or clipboard and opens the web browser to the
# Google Maps page for the address
# Usage: map_it <address>

import webbrowser
import sys
import pyperclip

if len(sys.argv) > 1:
    # Get address from command line
    address = ' '.join(sys.argv[1:])
else:
    # Get address from clipboard
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
