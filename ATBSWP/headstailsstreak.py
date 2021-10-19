import random

number_of_streaks = 0
coin_flip = []  # Initialise empty list to store Heads (0) or Tails (1) values
streak = 0

for experiment_number in range(1000):
    # Create list of 100 Heads (0) or Tails (1) values
    coin_flip.append(random.randint(0, 1))
    # Check the list for a streak of 6
    for i in range(len(coin_flip)):
        if coin_flip[i] == coin_flip[i-1]:
            streak += 1
        else:
            streak = 0
        if streak == 6:
            number_of_streaks += 1

print(f'Chance of streak: {number_of_streaks / 100}%')
