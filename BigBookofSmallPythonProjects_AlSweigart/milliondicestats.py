#!/user/bin/env python3
# milliondicestats.py - Simulates 1 million rolls of user-inputted amount of 6-sided dice and displays results

import random
import time

print('Million Dice Roll Statistics Simulator\n\nEnter how many six-sided dice you want to roll:')
while True:
    response = input('> ')
    if response.isdecimal():
        num_dice = int(response)
        break
    print('Please enter a number')

# Set up a dictionary to store the results of each dice roll
results = {}
for i in range(num_dice, (num_dice * 6) + 1):
    results[i] = 0

# Simulate dice rolls:
print(f'Simulating 1,000,000 rolls of {num_dice} dice...')
last_print_time = time.time()
for i in range(1000000):
    if time.time() > last_print_time + 1:
        print(f'{round(i / 10000, 1)}% done...')
        last_print_time = time.time()
    total = 0
    for j in range(num_dice):
        total = total + random.randint(1, 6)
    results[total] = results[total] + 1

# Display results
print('TOTAL - ROLLS - PERCENTAGE')
for i in range(num_dice, (num_dice * 6) + 1):
    roll = results[i]
    percentage = round(results[i] / 10000, 1)
    print(f'{i} - {roll} rolls - {percentage}%')
