# A proxy provides the same interface as the original object, but controls access to it. It can perform tasks before and after
# the original object is accessed. This is helpful when we want to implement memoization. We can use a cache proxy to copy the 
# object interface and then use the proxy class instead of the original class.

import time

# A Calculator object that could contain many more functions
class RawCalculator(object):
    def fib(self, n):
        if n < 2:
            return 1
        return self.fib(n-2) + self.fib(n-1)

# Takes a function as a parameter and returns a memoized version of that function. This function can be used with any function
# passed to it.
def memoize(fn):
    # Initialise an empty dictionary
    __cache = {}
    # Takes a list of args, gets the name of the function passed to it, and creates a tuple containg the function name and
    # the received args
    def memoized(*args):
        key = (fn.__name__, args)  # the tuple forms the key to the cache dictionary, and the value is the value returned  by the function
        # Check if the key is in the cache dict:
        if key in __cache:
            # If the key is in the dict, return the value
            return __cache[key]
        # If the key isn't in the dict, calculate the value by calling the function:
        __cache[key] = fn(*args)
        # Return the value
        return __cache[key]
    # Return the memoized function
    return memoized

# Takes the target object (RawCalculator()) as a parameter and sets an attribute on the proxy object, then overrides
# the fib(n) method with a memoized version of the method.
class CalculatorProxy(object):
    def __init__(self, target):
        self.target = target
        fib = getattr(self.target, 'fib')
        setattr(self.target, 'fib', memoize(fib))
    def __getattr__(self, name):
        return getattr(self.target, name)


if __name__ == "__main__":
    start = time.time()
    calculator = CalculatorProxy(RawCalculator())
    fib_sequence = [calculator.fib(x) for x in range(0, 80)]
    end = time.time()

    print(f'Calculating the list of {len(fib_sequence)} Fibonacci numbers took {end - start} seconds')



# Reference: 
# Badenhurst, Wessel. "Chapter 9: Proxy Pattern". Practical Python Design Patterns: Pythonic Solutions to Common Problems, Apress, October 20, 2017, pp. 133-141,
# DOI: https://doi.org/10.1007/978-1-4842-2680-3_9.