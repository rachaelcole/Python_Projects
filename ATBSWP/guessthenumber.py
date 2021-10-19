# Simple guess the number game
import random

secret_num = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')

# Ask the player to guess 6 times
for guesses in range(1, 7):
    print('Guess the number:')
    guess = int(input())
    if guess < secret_num:
        print('Too low. Guess again!')
    elif guess > secret_num:
        print('Too high. Guess again!')
    else:
        break  # break out of guessing loop

if guess == secret_num:
    print(f'You guessed it in {guesses} tries! The number was {secret_num}.')
else:
    print(f'Bzzt! Game over! The number I was thinking of was {secret_num}.')
