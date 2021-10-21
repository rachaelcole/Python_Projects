states = {
    'Australian Capital Territory': 'ACT',
    'Queensland': 'QLD',
    'New South Wales': 'NSW',
    'Northern Territory': 'NT',
    'South Australia': 'SA',
    'Tasmania': 'TAS',
    'Victoria': 'VIC',
    'Western Australia': 'WA'
}

cities = {
    'ACT': 'Canberra',
    'QLD': 'Brisbane',
    'NSW': 'Sydney',
    'NT': 'Darwin',
    'SA': 'Adelaide',
    'TAS': 'Hobart'}

cities['VIC'] = 'Melbourne'
cities['WA'] = 'Perth'

print('-' * 10)
print("SA has: ", cities['SA'])
print("VIC has: ", cities['VIC'])

print('-' * 10)
print("Queensland's abbreviation is: ", states['Queensland'])
print("Tasmania's abbreviation is: ", states['Tasmania'])

print('-' * 10)
print("Queensland has: ", cities[states['Queensland']])
print("Tasmania has: ", cities[states['Tasmania']])

print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} abbreviated is {abbrev}")

print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated to {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('-' * 10)
state = states.get('Victoria')

if not state:
    print('Sorry, no such state.')

city = cities.get('TX', 'Does not exist')
print(f"The city for the state 'TX' is {city}")
