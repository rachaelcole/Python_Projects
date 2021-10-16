import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)  # Randomly chooses something from the word.py list
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # Letters in the word stored as a set
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # What the user has guessed

    lives = 6

    # Getting user input
    while len(word_letters) > 0 and lives > 0:
        # Letters used
        print(f"You have {lives} lives left.\nYou have used these letters: ", ' '.join(used_letters))

        # What current word is (with dashes for unguessed letters)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word: ", ' '.join(word_list))

        user_letter = input("\nGuess a letter: ").upper()
        if user_letter in alphabet - used_letters:
                used_letters.add(user_letter)
                if user_letter in word_letters:
                    word_letters.remove(user_letter)
                else:
                    lives = lives - 1  # Takes away a life if wrong
                    print(f"\n'{user_letter}' is not in the word")
        elif user_letter in used_letters:
            print(f"\nYou have already guessed {user_letter}! Guess again.")
        else:
            print("\nInvalid character. Please try again.")

    # Gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print(f"\nUh oh, you died. The word was '{word}'. Try again!")
    else:
        print(f"\nCongratulations! You guessed the word '{word}'!")


print(hangman())
