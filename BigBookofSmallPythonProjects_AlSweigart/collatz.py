#!/user/bin/env python3
# collatz.py - Demonstrates the Collatz sequence, or the 3n + 1 problem, for a given number

import sys
import time

# Intro
print('''Collatz Sequence, or the 3n + 1 Problem

The Collatz Sequence is a sequence of numbers produced from a starting number, n, following three rules:

    1) If n is even, the next number n is n / 2.
    2) If n is odd, the next number n is n * 3 + 1.
    3) If n is 1, stop. Otherwise, repeat.

It is generally thought, but not mathematically proven, that every starting number n eventually terminates at 1.''')

# Get user input
print('Enter a number (greater than 0) or \'quit\':')
response = input('> ')
# If input isn't a number or is 0:
if not response.isdecimal() or response == '0':
    print('Please enter a valid number greater than 0')
    sys.exit()  # Quit
# Convert user input to an integer
n = int(response)
print(n, end='', flush=True)
# Collatz sequence:
while n != 1:  # continue until n == 1
    if n % 2 == 0:  # If n is even
        n = n // 2  # n = n/2
    else:   # If n is odd
        n = 3 * n + 1  # n = 3n + 1
    print(', ' + str(n), end='', flush=True)
    time.sleep(0.1)
print()
