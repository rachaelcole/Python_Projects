#!/user/bin/env python3
# caeserhacker.py - A simple Caesar Cipher hacking program
# A Caeser cipher is an ancient encryption algorithm that encrypts letters by shifting them over a certain number of
# places in the alphabet. The length of the shift is called the key. There are only 26 possible keys for a traditional
# (uppercase letters only) Caesar cipher, so we can easily use a brute-force attack to try every possible key for
# a standard Caeser cipher.

import string

print('Caesar Cipher Hacker')
print('Enter the encrypted Caesar cipher message to hack')
message = input('> ')
symbols = string.ascii_letters

for key in range(len(symbols)):  # Loop through every possible key
    translated = ''
    # Decrypt each symbol in the message
    for symbol in message:
        if symbol in symbols:
            num = symbols.find(symbol)  # Get the number of the symbol
            num = num - key  # Decrypt the number
            # Handle wrap around:
            if num < 0:
                num = num + len(symbols)
            # Add decrypted num's symbol to translated
            translated = translated + symbols[num]
        else:
            translated = translated + symbol
    # display the key being tested with its translated text
    print(f'Key #{key}: {translated}')
