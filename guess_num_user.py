import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)? ").lower()
        if feedback == "h":
            high = guess - 1
            print(f"Guess {guess} was too high. Guessing again...")
        if feedback == "l":
            low = guess + 1
            print(f"Guess {guess} was too low. Guessing again...")

    print(f"Yay, the computer guessed your number {guess} correctly!")

computer_guess(100)
