# This program says hello and asks for your name and age

print('Hello, world!')
print('What is your name? ')    # ask for their name
name = input()
print('Nice to meet you,', name)
print(f'The length of your name is {len(name)} letters.')
print('What is your age?')      # ask for their age
age = input()
print(f'You will be {str(int(age) + 1)} in a year.')
