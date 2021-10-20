# Ask user for sandwich preferences using pyinputplus, and display the total price of sandwiches

import pyinputplus as pyip

sandwich = {}

prices = {'wholemeal': 2.0, 'white': 1.0, 'sourdough': 2.5, 'chicken': 3.0, 'ham': 2.5, 'turkey': 3.5, 'tofu': 2.0,
          'swiss': 1.5, 'cheddar': 1.0, 'mozzarella': 1.75, 'mayo': 0.5, 'mustard': 0.5, 'lettuce': 0.5, 'tomato': 0.5}

num_sandwiches = 0
total_cost = 0
print('Welcome to the Sandwich Maker!')

make_sandwich = pyip.inputYesNo(prompt='Would you like to make a sandwich? Y/N ')

if make_sandwich == 'yes':
    # Choose bread
    bread = pyip.inputMenu(['wholemeal', 'white', 'sourdough'])
    sandwich['bread'] = bread
    total_cost += prices[bread]
    # Choose protein
    protein = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'])
    sandwich['protein'] = protein
    total_cost += prices[protein]
    # Choose cheese
    cheese = pyip.inputYesNo(prompt='Would you like to add cheese? Y/N ')
    sandwich['cheese'] = cheese
    if cheese == 'yes':
        # Choose kind of cheese
        cheese_type = pyip.inputMenu(['cheddar', 'swiss', 'mozzarella'])
        sandwich['cheese_type'] = cheese_type
        total_cost += prices[cheese_type]
    if cheese == 'no':
        cheese_type = 'none'
        sandwich['cheese_type'] = cheese_type
    # Choose mayo
    mayo = pyip.inputYesNo(prompt='Add mayonnaise? Y/N ')
    sandwich['mayo'] = mayo
    total_cost += prices['mayo']
    # Choose mustard
    mustard = pyip.inputYesNo(prompt='Add mustard? Y/N ')
    sandwich['mustard'] = mustard
    total_cost += prices['mustard']
    # Choose lettuce
    lettuce = pyip.inputYesNo(prompt='Add lettuce? Y/N ')
    sandwich['lettuce'] = lettuce
    total_cost += prices['lettuce']
    # Choose tomato
    tomato = pyip.inputYesNo(prompt='Add tomato? Y/N ')
    sandwich['tomato'] = tomato
    total_cost += prices['tomato']
    # How many sandwiches
    num_sandwiches = pyip.inputNum(prompt='How many sandwiches should I make? ')
    total_cost = total_cost * num_sandwiches
    print(f'''
Sandwich ordered:
    - {sandwich['bread']} bread
    - {sandwich['protein']}
    - cheese: {sandwich['cheese_type']}
    - mayo: {sandwich['mayo']}
    - mustard: {sandwich['mustard']}
    - lettuce: {sandwich['lettuce']}
    - tomato: {sandwich['tomato']}
    ''')
    print(f'Number of sandwiches ordered: {num_sandwiches}')
    print(f'Total price: ${total_cost:.2f}')
else:
    print('Goodbye!')




