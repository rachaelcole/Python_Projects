while True:                     # Infinite loop
    print('Who are you?')
    name = input().lower()
    if name != 'joe':           # if the user enters any name beside 'Joe', the continue statement starts the while
        continue                # loop again from the start
    print('Hello, Joe. What is the password? (Hint: a type of fish.)')
    password = input()
    if password == 'swordfish':
        break
print('Access granted.')
