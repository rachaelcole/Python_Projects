import sys


def collatz(number):
    if number % 2 == 0:
        sol = number // 2
        if sol == 1:
            print(sol)
            sys.exit()
        else:
            print(sol)
            return sol
    else:
        sol = 3 * number + 1
        if sol == 1:
            print(sol)
            sys.exit()
        else:
            print(sol)
            return sol


while True:
    user_input = input("Enter a number: ")
    try:
        user_input = int(user_input)
        collatz(user_input)
    except ValueError:
        print('Please enter digits only')



