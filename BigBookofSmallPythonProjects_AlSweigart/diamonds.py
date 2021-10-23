#!/user/bin/env python3
# diamonds.py - A small algorithm for drawing ASCII-art diamonds of various sizes. The user can choose either outlined
# or filled diamonds.


def display_outline_diamond(size):
    # Display the top half of the diamond
    for i in range(size):
        print(' ' * (size - i - 1), end='')  # Left-side space
        print('/', end='')  # Left side of diamond
        print(' ' * (i * 2), end='')  # Interior of diamond
        print('\\')  # Right side of diamond
    # Display the bottom half of the diamond
    for i in range(size):
        print(' ' * i, end='')  # Left side space
        print('\\', end='')  # Left side of diamond
        print(' ' * ((size - i - 1) * 2), end='')  # Interior of diamond
        print('/')  # Right side of diamond


def display_filled_diamond(size):
    # Display the top half of the diamond
    for i in range(size):
        print(' ' * (size - i - 1), end='')  # Left-side space
        print('/' * (i + 1), end='')  # Left half of diamond
        print('\\' * (i + 1))  # Right half of diamond
    # Display the bottom half of the diamond
    for i in range(size):
        print(' ' * i, end='')  # Left side space
        print('\\' * (size - i), end='')  # Left side of diamond
        print('/' * (size - i))  # Right side of diamond


def main():
    print('Diamonds')

    while True:
        # Prompt user for diamond type
        print('Would you like to print (o)utlined or (f)illed diamonds?')
        response = input('> ').lower()
        if response not in ('o', 'f'):
            print('Please enter a valid response: o (outlined) or f (filled)')
            continue
        else:
            # Prompt user for number of diamond sizes
            print('How many diamonds?')
            num_response = input('> ')
            if not num_response.isdecimal():
                print('Please enter a number')
                continue
            num_response = int(num_response)
            print(f'Displaying {num_response} diamonds...')
            if response == 'o':
                for i in range(num_response + 1):
                    display_outline_diamond(i)
            elif response == 'f':
                for i in range(num_response + 1):
                    display_filled_diamond(i)



if __name__ == '__main__':
    main()
