#!/user/bin/env/ python3
# vigenere.py - The Vigenère cipher, like a Caesar cipher but uses a multipart key

import pyperclip
import string

LETTERS = string.ascii_uppercase


def encrypt(message, key):
    return translate(message, key, 'encrypt')


def decrypt(message, key):
    return translate(message, key, 'decrypt')


def translate(message, key, mode):
    translated = []
    key_index = 0
    key = key.upper()
    for symbol in message:
        num = LETTERS.find(symbol.upper())
        if num != -1:
            if mode == 'encrypt':
                num += LETTERS.find(key[key_index])
            elif mode == 'decrypt':
                num -= LETTERS.find(key[key_index])
        num %= len(LETTERS)
        if symbol.isupper():
            translated.append(LETTERS[num])
        elif symbol.islower():
            translated.append(LETTERS[num].lower())
        key_index += 1
        if key_index == len(key):
            key_index = 0
        else:
            translated.append(symbol)
    return ''.join(translated)


def main():d
    """The Vigenère cipher is a polyalphabetic substitution cipher."""
    print('Vigenère Cipher')
    # Let user choose whether encrypting or decrypting:
    while True:
        print('Do you want to (e)ncrypt or (d)ecrypt?')
        response = input('> ').lower()
        if response.startswith('e'):
            mode = 'encrypt'
            break
        elif response.startswith('d'):
            mode = 'decrypt'
            break
        print('Please enter "e" for encryption or "d" for decryption.')

    # Let user specify the key to use
    while True:
        print('Please specify the key to use.\nIt can be a word or any combination of letters.')
        response = input('> ').upper()
        if response.isalpha():
            key = response
            break

    # Let the user specify the message to encrypt/decrypt
    print(f'Enter the message to {mode}:')
    message = input('> ')

    # Perform the encryption/decryption
    if mode == 'encrypt':
        translated = encrypt(message, key)
    elif mode == 'decrypt':
        translated = decrypt(message, key)

    print(f'{mode.title()}ed message: ')
    print(translated)

    pyperclip.copy(translated)
    print(f'Full {mode}ed text copied to clipboard.')


if __name__ == '__main__':
    main()
