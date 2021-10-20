import pyinputplus as pyip

while True:     # creates an infinite loop that runs until a break statement
    prompt = 'Want to know how to keep an idiot busy for hours? y/n '
    response = pyip.inputYesNo(prompt)
    if response == 'no':
        break

print('Thank you, have a nice day.')
