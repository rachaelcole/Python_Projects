import math
import random
from pcinput import get_float, get_integer, get_letter, get_string

# Functions
# each function has a name, and optional parameters/arguments and a return value

# title
print("{:^}\n".format("***CHAPTER 5: FUNCTIONS AND MODULES***"))

# format() is a method that 'works' on a string in this format: <string>.format()
print("Format method:")
print("The first 3 numbers are {}, {} and {}.".format("one", "two", "three"))
print("Backwards they are {2}, {1} and {0}.".format("one", "two", "three"))
print("The first 3 numbers are {}, {} and {}.".format("one", 2, 3.0))
print("The first 3 numbers are {:7}, {:7} and {:7}.".format("one", "two", "three"))  # assigning space
print("The first 3 numbers are {:4}, {:4} and {:4}.".format("one", "two", "three"))  # will take up space needed
print("The first 3 numbers are {:>7}, {:^7} and {:<7}.".format("one", "two", "three"))  # alignment
print("{} divided by {} is {}.".format(1, 2, 1/2))  # formatting numbers
print("{:d} divided by {:d} is {:f}.".format(1, 2, 1/2))
print("{:f} divided by {:f} is {:f}.".format(1, 2, 1/2))
print("{:5d} divided by {:5d} is {:5f}.".format(1, 2, 1/2))
print("{:<5f} divided by {:^5f} is {:>5f}.".format(1, 2, 1/2))
print("{:.2f} divided by {:.2f} is {:.2f}.".format(1, 2, 1/2))  # stating how many decimal points to go to
print('')

# making a table-like display with format():
s = "{:>5d} times {:>5.2f} is {:>5.2f}"
print(s.format(1, 3.75, 1 * 3.75))
print(s.format(2, 3.75, 2 * 3.75))
print(s.format(3, 3.75, 3 * 3.75))
print(s.format(4, 3.75, 4 * 3.75))
print(s.format(5, 3.75, 5 * 3.75))
print('')

# Modules: math, random, etc.
print("Modules:")
print("The value of e is approximately", math.exp(1))
e_sqr = math.exp(2)
print("e squared is", e_sqr)
print("which means that log(", e_sqr, ") is", math.log(e_sqr))

random.seed()
print("A random number between 1 and 10 is", random.randint(1, 10))
print("Another is", random.randint(1, 10))
random.seed(0)
print("3 random numbers are:", random.random(), random.random(), random.random())
random.seed(0)
print("The same 3 numbers are:", random.random(), random.random(), random.random())

# Custom module pcinput.py
print("Custom module pcinput.py")
num1 = get_integer("Please enter an integer: ")
num2 = get_integer("Please enter another integer: ")
print("The sum of", num1, "and", num2, "is", num1 + num2)
str1 = get_string("Please enter a string: ")
float1 = get_float(str1)
print("The float is", float1)
print('')

# Exercise 5.1: length of a string
print("Exercise 5.1: length of a string")
str1 = input("Please enter a string: ")
print(len(str1))

# Exercise 5.2: Pythagoras
print("Exercise 5.2: Pythagoras")
side1 = get_integer("Length of side 1: ")
side2 = get_integer("Length of side 2: ")
sum = side1**2 + side2**2
ans = math.sqrt(sum)
print("Length of side 3 is", ans)

# Exercise 5.3: min, max, avg
print("Exercise 5.3: min, max, average")
num1 = get_integer("Enter a number: ")
num2 = get_integer("Enter another number: ")
num3 = get_integer("Enter one more number: ")
print("Max is", max(num1, num2, num3))
print("Min is", min(num1, num2, num3))
avg = (num1 + num2 + num3) / 3
print("Average is", avg)

# Exercise 5.5: random num between 1 and 10 inclusive
print("Exercise 5.5: random number between 1 and 10 inclusive")
num1 = random.randint(0, 11)
print("Random number:", num1)

