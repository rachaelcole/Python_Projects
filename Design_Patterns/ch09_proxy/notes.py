# Proxy pattern

import time

# As programs grow, there are often functions that are called often. When these calculations are heavy or slow, the whole program
# suffers. Consider the following recursive Fibonacci sequence function:

def fib(n):
    if n < 2:
        return 1
    return fib(n - 2) + fib(n - 1)

# This function has a flaw: the value of f(x) would have to be calculated multiple times whenever you want to calculate a Fibonacci
# number for an n larger than 2. We can solve this problem with memoization.

# Memoization is the act of saving the result of a function call for later use.Caching the results as we go speeds the function up:

class Calculator(object):

    def fib_cached(self, n, cache):
        if n < 2:
            return 1
        try:
            result = cache[n]
        except:
            cache[n] = self.fib_cached(n - 2, cache) + self.fib_cached(n - 1, cache)  
            result = cache[n]
        return result
 
# We can see the effect of memoization on our fib(n) function as follows:

if __name__ == "__main__":
    cache = {}
    start = time.time()
    fib_sequence = [Calculator.fib_cached(x, cache) for x in range(0,40)]
    end = time.time()

    print(f'Calculating the list of {len(fib_sequence)} Fibonacci numbers took {end - start} seconds')






# Reference: 
# Badenhurst, Wessel. "Chapter 9: Proxy Pattern". Practical Python Design Patterns: Pythonic Solutions to Common Problems, Apress, October 20, 2017, pp. 133-141,
# DOI: https://doi.org/10.1007/978-1-4842-2680-3_9.