#! python3
# guessthenumber.py - A simple number-guessing game
# The computer randomly chooses a number between 1 and 100
# The computer gives users a hint to guess the number (hint costs 5 points)
# The user guesses a number (up to 10 guesses)
# If the guess is incorrect, the user loses a point
# If the guess is correct, the user gains 3 points and wins the round
# The game continues until the loser has 0 points, or has guessed 5 numbers correctly

import random
import pyinputplus as pyip


def get_hint(num):
      if num % 2 == 0:
            print("Hint: the number is a multiple of 2")
      elif num % 3 == 0:
            print("Hint: the number is a multiple of 3")
      elif num % 4 == 0:
            print("Hint: the number is a multiple of 4")
      elif num % 5 == 0:
            print("Hint: the number is a multiple of 5")

def play_game():
      # Initialise variables
      guesses = 0
      points = 10

      # Set random number to guess
      num_to_guess = random.randint(1, 100)

      # Start guess loop
      while guesses < 10:
            # Prompt user to input a number
            user_guess = pyip.inputNum('Guess a number: ')
            # Increment guess counter by 1
            guesses += 1

            # If user guesses the correct answer, add 3 points and win
            if user_guess == num_to_guess:
                  points += 3
                  print(f"You guessed it! The number was {num_to_guess}. You win!")
                  print(f'Points: {points}')
                  break
            # If user guesses an incorrect answer, remove 1 point and guess again
            else:
                  points -= 1
                  if user_guess < num_to_guess:
                        print(f'Too low! Guess again...')
                  elif user_guess > num_to_guess:
                        print('Too high! Guess again...')
                        print(f'Points: {points}\n')
                  # Ask user if they want a hint
                  if points >= 6:
                        get_hint_true = pyip.inputYesNo("Would you like a hint? It costs 5 points!! y/n: ")
                        if get_hint_true == 'yes':
                              points -= 5
                              get_hint(num_to_guess)
                              print(f'Points: {points}\n')
            # If the user's points reach zero, game over
            if points <= 0:
                  print(f'Game over! You ran out of points.')
                  break

      # If the user's guesses reach zero, game over
      if guesses == 0:
            print('Game over! You ran out of guesses.')


def main():
      # Welcome, title
      print("Welcome to Guess the Number!\n"
      "I am thinking of a number between 1 and 100...\n")
      play_again = 'yes'
      while play_again == 'yes':
            play_game()
            play_again = pyip.inputYesNo("Play again? y/n ")

main()
