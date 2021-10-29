from math import *
from expressions import *

"""
SYMBOLIC ALGEBRA

We can represent a mathematical function f(x) = (3x**2 + x)sin(x) as a function in Python:

def f(x):
    return (3*x**2 + x) * sin(x)

However, it is more useful to model algebraic expressions as data structures. This makes them
easier to manipulate.



MODELLING ALGEBRAIC EXPRESSIONS AS DATA STRUCTURES

Using our function f(x) = (3x**2 + x)sin(x) as an example, we can break it into bulding blocks:
    - A variable x
    - Numbers
    - Addition
    - Multiplication
    - A power
    - A specially-named function: sin(x)

We can translate these conceptual pieces into a data structure, a symbolic representation of the function.
See expressions.py to see the conceptual pieces translated into Python Classes, which all inherit from
an Abstract Base Class called Expression().


"""
# Exercises:


# Store the f expression from our example at the beginning as an object:
f_expression = Product(
    Sum(Product(Number(3),Power(Variable('x'),Number(2))),
    Variable('x')),
    Apply(Function('sin'),Variable('x')))

# Store another expression: cos(x**3 + -5)
g_expression = Apply(Function('cos'), Sum(Power(Variable('x'), Number(3)), Number(-5)))

# Store a log expression ln(y**z) as a data structure:
ln_expression = Apply(Function('ln'), Power(Variable('y'), Variable('z')))
log_expression = Apply(Function('log'), Power(Variable('y'), Variable('z')))  # log(y**z)

# Store (a+b)/2 as a Quotient object instance:
qt_expression = Quotient(Sum(Variable('a'), Variable('b')), Number(2))

# Get all the unique variables in f_expression:
vars = distinct_variables(f_expression)  # >> {'x'}

print(Product(Variable('x'), Variable('y')).evaluate(x=2,y=5))  # >> 10

print(f_expression.evaluate(x=5))
