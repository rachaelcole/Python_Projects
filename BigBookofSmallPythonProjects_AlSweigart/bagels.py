#!/user/bin/env python3
# bagels.py - A deductive logic game (based on string comparisons) where the user guesses a number based on clues.

import random
import string


NUM_DIGITS = 3  # (!) Try setting this to 1 or 10
MAX_GUESSES = 10  # (!) Try setting this to 1 or 100


def main():
    print(f'''Bagels, a deductive logic game.
    
I am thinking of a {NUM_DIGITS}-digit number with no repeated digits.
Try to guess what it is. Here are some clues:
When I say:     That means:
  pico          One digit is correct, but in the wrong position.
  fermi         One digit is correct and in the right position.
  bagels        No digit is correct.

For example, if the secret number was 248 and your guess was 843, the clues would be: Fermi Pico.''')

    while True:  # Main game loop
        # This stores the secret number the player needs to guess:
        secret_num = get_secret_num()
        print('I have thought up a number.')
        print(f'You have {MAX_GUESSES} guesses to get it.')

        num_guesses = 1
        while num_guesses < MAX_GUESSES:
            guess = ''
            # Keep looping until they enter a valid guess
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print(f'Guess #{num_guesses}: ')
                guess = input('> ')

            clues = get_clues(guess, secret_num)
            print(clues)
            num_guesses += 1

            if guess == secret_num:
                break  # They're correct, so break out of this loop
            if num_guesses > MAX_GUESSES:
                print('You ran out of guesses.')
                print(f'The answer was {secret_num}.')

        # Ask player if they want to play again
        print('Do you want to play again? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break
    print('Thanks for playing!')


def get_secret_num():
    # Returns a string made up of NUM_DIGITS unique random digits
    numbers = list(string.digits)  # Create a list of digits
    random.shuffle(numbers)  # Shuffle them into random order

    # Get the first NUM_DIGITS digits in the list for the secret number:
    secret_num = ''
    for i in range(NUM_DIGITS):
        secret_num += str(numbers[i])
    return secret_num


def get_clues(guess, secret_num):
    # Returns a string with the pico, fermi, bagels clues for a guess and secret number pair
    if guess == secret_num:
        return 'You got it!'
    clues = []
    for i in range(len(guess)):
        if guess[i] == secret_num[i]:
            # A correct digit is in place
            clues.append('fermi')
        elif guess[i] in secret_num:
            # A correct digit is in the incorrect place
            clues.append('pico')
    if len(clues) == 0:
        return 'bagels'  # There are no correct digits at all
    else:
        # Sort the clues into alphabetical order
        clues.sort()
        # Make a single string from the list of string clues
        return ' '.join(clues)

# If the program is run (instead of imported), run the game:
if __name__ == "__main__":
    main()
