#!/user/bin/env python3
# fibonacci.py - Prints out Fibonnaci sequences

import sys

print('Fibonacci Sequence')

while True:
    while True:
        print('Enter the nth Fibonacci number you wish to calculate to, or \'quit\' to quit')
        response = input('> ').upper()
        if response == 'QUIT':
            sys.exit()
        if response.isdecimal() and int(response) != 0:
            nth = int(response)
            break
        print('Please enter a number greater than 0, or \'quit\' to quit')
    print()
    if nth == 1:
        print('0')
        print()
        print('The #1 Fibonacci number is 0.')
        continue
    elif nth == 2:
        print('0, 1')
        print()
        print('The #2 Fibonacci number is 1.')
    if nth > 10000:
        print('WARNING: This will take a while to display to the screen. Press Ctrl-C to quit any time.')
        print('Press Enter to begin...')
    second_last = 0
    last = 1
    fibs = 2
    print('0, 1, ', end='')
    while True:
        next_num = second_last + last
        fibs += 1
        print(next_num, end='')
        if fibs == nth:
            print(f'\n\nThe #{fibs} Fibonacci number is {next_num}', sep='')
            break
        print(', ', end='')
        second_last = last
        last = next_num
