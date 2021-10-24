#!/user/bin/env python3
# timestables.py - Prints a multiplication table from 1x1 to 12x12

print('Times Tables')
print('  |  1   2   3   4   5   6   7   8   9  10   11  12')
print('--+------------------------------------------------')

# Display each row of products
for num1 in range(1, 13):
    # Print the vertical labels
    print(str(num1).rjust(2), end='')
    # Print a separating bar
    print('|', end='')
    for num2 in range(1, 13):
        # Print the product and a space
        print(str(num1 * num2).rjust(3), end=' ')
    print()
