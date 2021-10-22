import random
import string
import pyinputplus


# Generate a random letters (based on ASCII, string methods) and shuffle into a password
def get_password(num):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for i in range(num))
    print(f'Your randomly generated password is: {password}')


def main():
    print("Welcome to the password generator!")
    get_another_password = 'yes'
    while get_another_password == 'yes':
        num = pyinputplus.inputNum('How many characters should the password be? ')
        get_password(num)
        get_another_password = pyinputplus.inputYesNo('Get another password? y/n: ')
    print("Bye!")


main()
