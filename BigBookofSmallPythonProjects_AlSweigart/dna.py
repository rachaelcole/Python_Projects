#!/user/bin/env python3
# dna.py - A DNA double-helix animation
import random, time, sys

PAUSE = 0.15
ROWS = [
    '       ##',  # Index 0 has no {}
    '     #{}-{}#',
    '    #{}---{}#',
    '   #{}-----{}#',
    '  #{}------{}#',
    ' #{}------{}#',
    ' #{}-----{}#',
    ' #{}---{}#',
    ' #{}-{}#',
    '  ##',  # Index 9 has no {}.
    ' #{}-{}#',
    ' #{}---{}#',
    '#{}-----{}#',
    ' #{}------{}#',
    '  #{}------{}#',
    '   #{}-----{}#',
    '    #{}---{}#',
    '      #{}-{}#']

try:
    print('DNA Animation\n'
          'Press Ctrl-C to quit.')
    time.sleep(2)
    row_index = 0
    while True:  # Main program loop
        row_index = row_index + 1
        if row_index == len(ROWS):
            row_index = 0
        # Row indexes 0 and 9 don't have nucleotides:
        if row_index == 0 or row_index == 9:
            print(ROWS[row_index])
            continue
        # Select random nucleotide pairs
        random_selection = random.randint(1, 4)
        if random_selection == 1:
            left_nuc, right_nuc = 'A', 'T'
        elif random_selection == 2:
            left_nuc, right_nuc = 'T', 'A'
        elif random_selection == 3:
            left_nuc, right_nuc = 'C', 'G'
        elif random_selection == 4:
            left_nuc, right_nuc = 'G', 'C'
        # Print the row
        print(ROWS[row_index].format(left_nuc, right_nuc))
        time.sleep(PAUSE)
except KeyboardInterrupt:
    sys.exit()
