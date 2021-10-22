#!/user/bin/env python3
# birthdayparadox.py - A Birthday Paradox simulation

import datetime
import random


def get_birthdays(num_birthdays):
    """Returns a list of number random date objects for birthdays."""
    birthdays = []
    for i in range(num_birthdays):
        # The year is unimportant for the simulation, as long as all birthdays have the same year
        start_year = datetime.date(2001, 1, 1)
        # Get a random day into the year
        random_days = datetime.timedelta(random.randint(0, 364))
        birthday = start_year + random_days
        birthdays.append(birthday)
    return birthdays


def get_match(birthdays):
    """Returns the date object of a birthday that occurs more than once in the birthdays list."""
    if len(birthdays) == len(set(birthdays)):
        return None  # All birthdays are unique, so return None
    # Compare each birthday to every other birthday:
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a + 1 :]):
            if birthdayA == birthdayB:
                return birthdayA    # Return the matching birthday


# Display the intro
print("""Birthday Paradox
The Birthday Paradox (n.b., not actually a paradox) shows us that in a group of N people, the odds that two of 
them have matching birthdays is surprisingly large.

This program does a Monte Carlo simulation (i.e., repeated random simulations) to explore this concept.\n""")

# Set up a tuple of the month names in order:
MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

while True:  # Keep asking until the user enters a valid amount
    print('How many birthdays should I generate? (max 100)')
    response = input('> ')
    if response.isdecimal() and (0 < int(response) <= 100):
        num_bdays = int(response)
        break  # The user has entered a valid amount
print()

# Generate and display the birthdays
print(f'Here are {num_bdays} birthdays:')
birthdays = get_birthdays(num_bdays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        # Display a comma for each birthday after the first birthday
        print(', ', end='')
    month_name = MONTHS[birthday.month - 1]
    date_text = f'{month_name} {birthday.day}'
    print(date_text, end='')
print()
print()

# Determine if there are two birthdays that match
match = get_match(birthdays)

# Display the results:
print('In this simulation, ', end='')
if match is not None:
    month_name = MONTHS[match.month - 1]
    date_text = f'{month_name} {match.day}'
    print(f'multiple people have a birthday on {date_text}.')
else:
    print('there are no matching birthdays.')
print()

# Run through 100,000 simulations
print(f'Generating {num_bdays} random birthdays 100,000 times...')
input('Press Enter to begin...')

print(f"Let's run another 100,000 simulations.")
sim_match = 0  # How many simulations had matching birthdays in them
for i in range(100000):
    # Report on the progress every 10,000 simulations:
    if i % 10000 == 0:
        print(f'{i} simulations run...')
    birthdays = get_birthdays(num_bdays)
    if get_match(birthdays) is not None:
        sim_match = sim_match + 1
print('100,000 simulations run.')

# Display simulation results
probability = round(sim_match / 100000 * 100, 2)
print(f'Out of 100,000 simulations of {num_bdays} people, there was a matching birthday in that group {sim_match} '
      f'times. \nThis means that {num_bdays} people have a {probability}% chance of having a matching birthday in their'
      f' group. \n'
      f'That\'s probably more than you would think!')
