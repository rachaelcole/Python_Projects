# Decorators

# To decorate a function, we need to return an object that can be used as a function (i.e. any object with a __call__ method). 
# A decorator is a unary function (takes a single argument) that takes a function to be decorated as its argument. It then returns
# a function that is the same as the original function with some added functionality. We can stack decorators. Python has built-in 
# syntax for decorators, using the @ symbol. We can use classes or functions to define decorators.

# In the following example, we will decorate a Fibonnaci function with a timer function using a function.

import time


def profiling_decorator(f):
    # Returns a function to be used (wrapped_f) when this decorator function is called
    def wrapped_f(n):
        # Wrap the running of the function in time requests
        start = time.time()
        result = f(n)
        end = time.time()
        # Print time elapsed to console just prior to returning
        print(f'Time elapsed for n = {n}: {end - start}')
        return result
    return wrapped_f

@profiling_decorator
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