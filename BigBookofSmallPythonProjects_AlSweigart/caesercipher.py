#!/user/bin/env python3
# caesercipher.py - A simple Caesar Cipher program
# A Caeser cipher is an ancient encryption algorithm that encrypts letters by shifting them over a certain number of
# places in the alphabet. The length of the shift is called the key.

import pyperclip
import string

# Every possible symbol that can be encrypted/decrypted
symbols = string.ascii_letters # + string.digits + string.punctuation
print('Caesar Cipher')
print('The Caesar Cipher encrypts letters by shifting them over in the alphabet by a key number.')
print()

# Let the user enter if they are encrypting or decrypting:
while True:  # Keep asking until the user enters a valid input
    print('Do you want to (e)ncrypt or (d)ecrypt?')
    response = input('> ').lower()
    if response.startswith('e'):
        mode = 'encrypt'
        break
    elif response.startswith('d'):
        mode = 'decrypt'
        break
    print('Please enter either e (for encrypt) or d (for decrypt).')

# Let the user enter the key to use:
while True:
    max_key = len(symbols) - 1
    print(f'Please enter the key (0 to {max_key}) to use')
    response = input('> ').upper()
    if not response.isdecimal():
        continue
    if 0 <= int(response) < len(symbols):
        key = int(response)
        break

# Let the user enter the message to encrypt/decrypt
print(f'Enter the message to {mode}')
message = input('> ')
# Caesar cipher only works on uppercase letters
# message = message.upper()
# Store the encrypted/decrypted form of the message:
translated = ''
# Encrypt/decrypt each symbol in the message:
for symbol in message:
    if symbol in symbols:
        # Get the encrypted/decrypted number for this symbol
        num = symbols.find(symbol)  # Get the number of the symbol
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num - key
        # Handle the wrap-around if num >= len(symbols) or num < 0
        if num >= len(symbols):
            num = num - len(symbols)
        elif num < 0:
            num = num + len(symbols)

        # Add the encrypted/decrypted num's symbol to translated
        translated = translated + symbols[num]
    else:
        # Just add the symbol without encrypting/decrypting
        translated = translated + symbol

# Display the encrypted/decrypted string to the screen:
print(translated)
pyperclip.copy(translated)
print(f'Full {mode}ed text copied to clipboard.')
