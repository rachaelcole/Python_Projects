# user/bin/env/python3
# sevseg.py - Displays a seven-segment display module for numbers

"""
A labeled seven-segment display, with each segment labeled A to G.
  __A__
 |    |
 F    B
|__G__|
|     |
E     C
|__D__|

 __     __  __        __  __   __   __   __
|  | |  __| __| |__| |__ |__     | |__| |__|
|__| | |__  __|    |  __||__|    | |__|  __|
"""

def get_sev_seg_str(num, min_width=0):
    """Return a seven-segment display with a string of num. The returned string will be padded with 0s if it is smaller
    than min_width."""
    # Convert number to string in case it's an int or float:
    num = str(num).zfill(min_width)
    rows = ['', '', '']
    for i, numeral in enumerate(num):
        if numeral == '.':  # Render the decimal point
            rows[0] += ' '
            rows[1] += ' '
            rows[2] += '.'
            continue  # Skip the space in between digits
        elif numeral == '-':  # Render the negative sign
            rows[0] += '    '
            rows[1] += ' __ '
            rows[2] += '    '
        elif numeral == '0':  # Render the 0
            rows[0] += ' __ '
            rows[1] += '|  |'
            rows[2] += '|__|'
        elif numeral == '1':  # Render the 1
            rows[0] += '    '
            rows[1] += '   |'
            rows[2] += '   |'
        elif numeral == '2':  # Render the 2
            rows[0] += ' __ '
            rows[1] += ' __|'
            rows[2] += '|__ '
        elif numeral == '3':  # Render the 3
            rows[0] += ' __ '
            rows[1] += ' __|'
            rows[2] += ' __|'
        elif numeral == '4':  # Render the 4
            rows[0] += '    '
            rows[1] += '|__|'
            rows[2] += '   |'
        elif numeral == '5':  # Render the 5
            rows[0] += ' __ '
            rows[1] += '|__'
            rows[2] += ' __|'
        elif numeral == '6':  # Render the 6
            rows[0] += ' __ '
            rows[1] += '|__ '
            rows[2] += '|__|'
        elif numeral == '7':  # Render the 7
            rows[0] += ' __ '
            rows[1] += '   |'
            rows[2] += '   |'
        elif numeral == '8':  # Render the 8
            rows[0] += ' __ '
            rows[1] += '|__|'
            rows[2] += '|__|'
        elif numeral == '9':  # Render the 9
            rows[0] += ' __ '
            rows[1] += '|__|'
            rows[2] += ' __|'

        # Add a space (for the space in between numerals) if this isn't the last numeral
        if i != len(num) - 1:
            rows[0] += ' '
            rows[1] += ' '
            rows[2] += ' '
    return '\n'.join(rows)

if __name__ == '__main__':
    print('This module is designed to be imported rather than run.')
    print('For example, this code:')
    print('    import sevseg')
    print('    my_number = sevseg.get_sev_seg_str(42, 3)')
    print('    print(my_number)')
    print()
    print('... will print 42, zero-padded to three digits:')
    print(' __        __ ')
    print('|  | |__|  __|')
    print('|__|    | |__ ')
    print()
    my_num = get_sev_seg_str(55, 3)
    print(my_num)
