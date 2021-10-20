#! python3
# mclip_v2.pyw - Saves and loads pieces of text to the clipboard
# Usage: py.exe mclip_v2.pyw save <keyword> - Saves clipboard to keyword
#        py.exe mclip_v2.pyw <keyword>      - Loads keyword to clipboard
#        py.exe mclip_v2.pyw list           - Loads all keywords to clipboard
#        py.exe mclip_v2.pyw delete <keyword> - Deletes keyword from shelf file
#        py.exe mclip_v2.pyw delete           - Deletes all keywords from shelf file

import shelve
import pyperclip
import sys

mclip_shelf = shelve.open('mclip_v2_')           # Shelf file will be named with prefix 'mclip_v2_'

if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    # Save clipboard content
    mclip_shelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    # Delete keyword from shelf file
    del mclip_shelf[sys.argv[2]]
elif len(sys.argv) == 2:
    # List keywords and load content
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mclip_shelf.keys())))
    elif sys.argv[1].lower() == 'delete':
        # Delete all keywords from mclip_shelf file
        mclip_shelf.clear()
    elif sys.argv[1] in mclip_shelf:
        pyperclip.copy(mclip_shelf[sys.argv[1]])

mclip_shelf.close()
