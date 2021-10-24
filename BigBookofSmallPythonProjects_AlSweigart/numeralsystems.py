#!/user/bin/env python3
# numeralsystems.py - Displays numbers in decimal, binary, octal, and hexadecimal

print('Numeral System Counters\n\nThis program shows you equivalent numbers in decimal (base 10), binary (base 2),'
      'and hexadecimal (base 16) numeral systems.\n\n(Ctrl-C to quit.)\n')
while True:
    response = input('Enter the starting number (e.g. 0): ')
    if response == '':
        response = '0'
        break
    if response.isdecimal():
        break
    print('Please enter a number greater than or equal to 0.')
start = int(response)
while True:
    response = input('Enter how many numbers to display (e.g. 1000): ')
    if response == '':
        response = '1000'
        break
    if response.isdecimal():
        break
    print('Please enter a number greater than 0.')
amount = int(response)
for num in range(start, start + amount):
    hexnum = hex(num)[2:].upper()
    binnum = bin(num)[2:]
    octnum = oct(num)[2:]
    print(f'DEC: {num}      HEX: {hexnum}      OCT: {octnum}      BIN: {binnum}')
