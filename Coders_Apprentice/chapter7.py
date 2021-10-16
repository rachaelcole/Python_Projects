from math import sqrt
import random
import time
from pcinput import get_float, get_integer, get_letter, get_string


# title
print("{:^}\n".format("***CHAPTER 7: ITERATIONS***"))
print("")

# Exercise 7.1.1: while loop
print("Exercise 7.1.1: introducing while loops")
num = 1                 # Initialises the variable 'num' to 1
while num <= 5:         # while num is less than or equal to 5:
    print(num)             # print num
    num += 1            # increment num by 1, and go back to start of loop, until num =5
print("Done!")          # after printing num=5, we break out of loop and run this line
print("")

# Exercise 7.1.2: another while loop
print("Exercise 7.1.2: while loop -> asking for user input")
total = 0
count = 0
while count < 5:
    total += get_integer("Please enter a number: ")
    count += 1
    average = total / count
print("Total is", total)
print("Average is", average)
print("")


# Exercise 7.1.5 a: while loop practice
print("Exercise 7.1.5 a: Countdown Timer")
val = 10
while val > 0:
    print(f"{val}... ")
    val -= 1
    time.sleep(0.8)
print("Blast off!")



print("")
# Exercise 7.1.5 b: factorials
print("Exercise: 7.1.5 b: factorials")
user_num = get_integer("Enter a number from 1 to 10: ")
user_inp = user_num
if user_num < 1 or user_num > 10:
    print("Invalid number. Enter a number from 1 to 10.")
# factorials:
factorial = 1
while user_num > 1:
    factorial = factorial * user_num
    user_num = user_num - 1
print(f"The factorial of {user_inp} is {factorial}.")



print("")
# Exercise 7.2 b: for loop
print("Exercise: 7.2: for loops")
# for <variable> in <collection>:
#   <statements>
# for loop over a string:
fruit = "banana"
for letter in fruit:
    print(letter)
print("Done.\n")

# for loop using range()
for x in range(10):
    print(x)
print("Done.\n")

# range min, max, step:
for x in range(1,20,2):
    print(x)
print("Done.\n")

# counting in multiples of 3, starting at 21, down to 3
for x in range(21,0,-3):
    print(x)
print("Done.\n")

print("")
# Exercise 7.2.4: for loop with manual collections; iterates through all items in tuples
print("Exercise: 7.2.4: for loops with manual collections")
for x in (10, 100, 1000, 10000):
    print(x)
print("Done.\n")

for x in ("apple", "pear", "orange", "banana", "mango", "cherry"):
    print(x)
print("Done.\n")


print("")
# Exercise: 7.2.5: Practicing using for loops
print("Exercise: 7.2.5: Practicing using for loops")
# Ask user for input 5 times and return sum of 5 inputs
total = 0
for x in range(0,5):
    inp = get_integer("Enter a number: ")
    total = total + inp
print(total)
print("Done.\n")

# Make a countdown timer
for x in range(10, 0, -1):
    print(f"{x}...")
    time.sleep(0.8)
print("Blast off! \n")
