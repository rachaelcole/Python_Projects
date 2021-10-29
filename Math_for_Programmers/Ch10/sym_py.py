from expressions import *
from math import *
from sympy import *
from sympy.core.core import *

# SymPy is a robust Python library for working with algebraic expressions in Python code

ex1 = Mul(Symbol('y'),Add(3,Symbol('x')))
print(ex1)

y = Symbol('y')
x = Symbol('x')

print(y*(3+x))

print(y*(3+x).subs(x,1))

print((x**2).diff(x))

print((3*x**2).integrate(x))

print(Integer(0).integrate(x))

print((x*cos(x)).integrate(x))

print((x**2).integrate(x))