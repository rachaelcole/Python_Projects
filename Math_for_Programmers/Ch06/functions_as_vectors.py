import numpy as np
import matplotlib.pyplot as plt
from math import sin
from colors import *
from vectors import *
from classes import *
from matrices import *
from tests import *

# Class representing a function as a vector
class Function(Vector):
    def __init__(self, f):
        self.function = f
    def add(self, other):
        return Function(lambda x: self.function(x) + other.function(x))
    def scale(self, scalar):
        return Function(lambda x: scalar * self.function(x))
    @classmethod
    def zero(cls):
        return Function(lambda x: 0)
    # Lets us treat this as a function:
    def __call__(self, arg):
        return self.function(arg)


# Stores a function of 2 variables ike f(x, y) = x + y
class Function2(Vector):
    def ___init__(self, f):
        self.function = f
    def add(self, other):
        return Function(lambda x,y: self.function(x,y) + other.function(x,y))
    def scale(self, scalar):
        return Function(lambda x,y: scalar * self.function(x,y))
    @classmethod
    def zero(cls):
        return Function(lambda x,y: 0)
    def __call__(self, *args):
        return self.function(*args)



# Class representing a polynomial as a vector:
class Polynomial(Vector):
    def __init__(self, *coefficients):
        self.coefficients = coefficients
    def __call__(self, x):
        return sum(coefficient * x ** power for (power, coefficient) in enumerate(self.coefficients))
    def add(self, p):
        return Polynomial([a+b for a,b in zip(self.coefficients, p.coefficients)])
    def scale(self, scalar):
        return Polynomial([scalar * a for a in self.coefficients])
    def _repr_latex_(self):
        monomials = [repr(coefficient) if power == 0
        else "x ^ {%d}" % power if coefficient == 1
        else "%s x ^ {%d}" % (coefficient, power)
        for (power, coefficient) in enumerate(self.coefficients)
        if coefficient != 0]
        return "$ %s $" % (" + ".join(monomials))
    @classmethod
    def zero(cls):
        return Polynomial(0)


"""
Mathematical functions that take in  a single real number and output a single real number can be thought of as vectors: f: R -> R
In Python, we can consider this functions that take float values in and return float values.
"""

# Plotting function that draws the graph of one or more functions on a specified range of inputs
def plot(fs, xmin, xmax):
    xs = np.linspace(xmin,xmax,100)
    fig, ax = plt.subplots()
    ax.axhline(y=0, color='k')
    ax.axvline(x=0, color='k')
    for f in fs:
        ys = [f(x) for x in xs]
        plt.plot(xs, ys)

# Sample functions to demonstrate our plot() function
def f(x):
    return 0.5 * x + 3

def g(x):
    return sin(x)

# Plots the f(x) and g(x) functions on x values between -10 and 10:
plot([f,g],-10,10)

"""
Algebraically, f + g is a function defined by (f + g)(x) = f(x) + g(x) = 0.5 * x + 3 + sin(x)
Graphically, the y-values of each point are added. 
We can visualise this by defining a function that adds our functions and returns a new function which 
is their sum.
"""

def add_functions(f, g):
    def new_function(x):
        return f(x) + g(x)
    return new_function

# Plot the f(x), g(x), and added (f+g)(x) functions on x-vals from -10 to 10:
plot([f, g, add_functions(f,g)], -10, 10)

"""
We can multiply a function by its scalar by multiplying its expression by the scalar:
3g is defined by: (3g)(x) = 3 * g(x) = 3 * sin(x)
This stretches the graph of the function g in the y direction by a factor of 3.
"""

f = Function(lambda x: 0.5 * x + 3)
g = Function(sin)

plot([f,g,f+g,3*g], -10, 10)

# Test whether two functions are equal
def approx_equal_function(f,g):
    results = []
    for _ in range(0, 10):
        x = uniform(-10,10)
        results.append(isclose(f(x),g(x)))
    return all(results)


# Get a random Polynomial function
def random_function():
    degree = randint(0,5)
    p = Polynomial(*[uniform(-10, 10) for _ in range(0, degree)])
    return Function(lambda x: p(x))

# Run a unit test for function equality using the above random_function() 
for i in range(0,100):
    a,b = random_scalar(), random_scalar()
    u,v,w = random_function(), random_function(), random_function()
    test(Function.zero(), approx_equal_function, a,b,u,v,w)