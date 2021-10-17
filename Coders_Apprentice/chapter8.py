from math import sqrt
import datetime
import random
import time
from pcinput import get_float, get_integer, get_letter, get_string


# title
print("{:^}\n".format("***CHAPTER 8: FUNCTIONS***"))
print("")

# 8.2.: Creating functions
print("8.2. Creating functions")
# def <function name>(<parameters>):
#     <statements>


def goodbye_world():
    print("Goodbye, world!")


print("Hello, world!")
goodbye_world()

print("")
# 8.2.3: Parameter types
print("8.2.3. Parameter types")
a = "Hello"
if isinstance(a, int):
    print("integer")
elif isinstance(a, float):
    print("float")
elif isinstance(a, str):
    print("string")
else:
    print("other")

print("")
# 8.2.5. return
print("8.2.5. return")
# <variable> = <function>()
# return <result> will store the result of <function>() in <variable>


def pythagoras(a , b):
    if a <= 0 or b <= 0:
        return -1
    return sqrt(a * a + b * b)


num1 = get_integer("Give side 1: ")
num2 = get_integer("Give side 2: ")
num3 = pythagoras(num1, num2)

if num3 < 0:
    print("The numbers you provided cannot be used.")
else:
    print("The diagonal side's length is", num3)


print("")
# 8.2.8. Multiple return values
print("8.2.8. Multiple return values")


def add_days(year, month, day, dayincrement):
    startdate = datetime.datetime(year, month, day)
    enddate = startdate + datetime.timedelta(days=dayincrement)
    return enddate.year, enddate.month, enddate.day


y, m, d = add_days(2015, 11, 13, 55)
print("{}/{}/{}".format(d, m, y))



print("")
# 8.2.10. Naming functions
print("8.2.10. Naming functions")


def isEven(x):
    if x % 2 == 0:
        print(f'{x} is even')
    else:
        print(f'{x} is odd')


isEven(12)
isEven(55)


print("")
# 8.6. Anonymous functions
print("8.6. Anonymous functions")

# lambda <parameters>: <statement>

f = lambda x: x*x
print(f(12))


print("")
# Exercise 8.1.
print("Exercise 8.1.")

def tables(num):
    i = 1
    while i < 13:
        print(f'{i} * {num} = {num*i}')
        i += 1

tables(6)
