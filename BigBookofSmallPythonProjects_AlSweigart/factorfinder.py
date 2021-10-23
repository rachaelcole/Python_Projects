#!/user/bin/env python3
# factorfinder.py - Returns the factors of a number

import math, sys

print('''Factor Finder

A number's factors are two numbers that, when multiplied with each other, produce the number. Prime numbers have only
two factors (1 and itself).''')

while True:
    print('Enter a positive whole number to factor (or \'quit\' to quit):')
    response = input("> ")
    if response.upper() == 'QUIT':
        sys.exit()
    if not (response.isdecimal() and int(response) > 0):
        continue
    number = int(response)
    factors = []
    for i in range(1, int(math.sqrt(number)) + 1):
        if number % i == 0:
            factors.append(i)
            factors.append(number // i)
    factors = list(set(factors))
    factors.sort()
    for i, factor in enumerate(factors):
        factors[i] = str(factor)
    print(', '.join(factors))
