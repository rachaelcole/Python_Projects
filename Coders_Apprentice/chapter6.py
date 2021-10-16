from math import sqrt
import random
from pcinput import get_float, get_integer, get_letter, get_string

# Boolean expressions
# title
print("{:^}\n".format("***CHAPTER 6:CONDITIONALS***"))
print("")

print("Exercise 6.1: ")
# Grades are values between 0 and 10 inclusive, rounded to the nearest half point
# A = 8.5 - 10.0
# B = 7.5 - 8.0
# C = 6.5 - 7.0
# D = 5.5 - 6.0
# F = 0.0 - 5.0
user_input = get_float("Enter a grade between 0.0 and 10.0: ")

if user_input < 0 or user_input > 10.0:
    print("Invalid grade. Please enter a grade between 0.0 and 10.0.")
else:
    if user_input < 11 and user_input > 8.0:
        print("Your grade is an A")
    elif user_input < 8.5 and user_input > 7.0:
        print("Your grade is a B")
    elif user_input < 7.5 and user_input > 6.0:
        print("Your grade is a C")
    elif user_input < 6.5 and user_input > 5.5:
        print("Your grade is a D")
    else:
        print("Your grade is an F")


print('')
print('')

print("Exercise 6.3:")
num_vowels = 0
user_string = get_string("Enter a string: ").lower()
if 'a' in user_string:
    num_vowels += 1
if 'e' in user_string:
    num_vowels += 1
if 'i' in user_string:
    num_vowels += 1
if 'o' in user_string:
    num_vowels += 1
if 'u' in user_string:
    num_vowels += 1
if num_vowels == 1:
    print(f"There is one vowel in the string.")
else:
    print(f"There are {num_vowels} different vowels in the string.")



print('')
print('')

print("Exercise 6.4: Quadratic Equation")
# Formula: Ax**2 + Bx + C = 0
# Has 0, 1, or 2 solutions:
# First solution:  (-B + sqrt(B**2 - 4AC))/(2A)
# Second solution: (-B - sqrt(B**2 - 4AC))/(2A)
# 0 solutions if the value under the square root is negative
# 1 solution  if the value under the square root is zero
# 2 solutions if the value under the square root is positive

var_A = get_integer("Enter an number: ")
var_B = get_integer("Enter a second number: ")
var_C = get_integer("Enter a third number: ")
var_X = (var_B**2) - (4*var_A*var_C)
sqrtval = sqrt(abs(var_X))

if var_X < 0:
    print("There are no solutions.")
elif var_X == 0:
    print("There is one solution:")
    sol1 = ((-1 * var_B) + sqrtval) / (2 * var_A)
    print(sol1)
else:
    print("There are two solutions:")
    sol3 = ((-1 * var_B) + sqrtval) / (2 * var_A)
    sol4 = ((-1 * var_B) - sqrtval) / (2 * var_A)
    print(sol3)
    print(sol4)
