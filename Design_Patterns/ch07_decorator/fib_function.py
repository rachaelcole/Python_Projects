# Decorators

# To decorate a function, we need to return an object that can be used as a function (i.e. any object with a __call__ method). 
# A decorator is a unary function (takes a single argument) that takes a function to be decorated as its argument. It then returns
# a function that is the same as the original function with some added functionality. We can stack decorators. Python has built-in 
# syntax for decorators, using the @ symbol. We can use classes or functions to define decorators.

# In the following example, we will decorate a Fibonnaci function with a timer function using a class.

import time

class ProfilingDecorator(object):
    def __init__(self, f):
        print('Profiling decorator initiated')
        # The decorated function is saved as an attribute of the object during init
        self.f = f
    def __call__(self, *args):
        # Wrap the running of the function in time requests
        start = time.time()
        result = self.f(*args)
        end = time.time()
        # Print time elapsed to console just prior to returning
        print(f'Time elapsed for n = {n}: {end - start}')
        return result

# The decorator initiates an object and passes in the function being wrapped as an arg to the constructor
# The returned object has the __call__() method
@ProfilingDecorator
def fib(n):
    print('Inside fib(n)')
    if n < 2:
        return
    fib_prev = 1
    fib = 1
    for num in range(2, n):
        fib_prev, fib = fib, fib + fib_prev
    return fib


if __name__ == "__main__":
    n = 77
    print(f'Fibonacci number for n = {n}: {fib(n)}')


# Reference: 
# Badenhurst, Wessel. "Chapter 7: Decorator Pattern". Practical Python Design Patterns: Pythonic Solutions to Common Problems, Apress, October 20, 2017, pp. 105-121,
# DOI: https://doi.org/10.1007/978-1-4842-2680-3_7.