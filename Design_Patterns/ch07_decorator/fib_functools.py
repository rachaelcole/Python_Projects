import time
from functools import wraps

# General wrapper for any maths function
def profiling_wrapper(f):
    @wraps(f)
    def wrap_f(*args, **kwargs):
        start = time.time()
        result = f(*args, **kwargs)
        end = time.time()
        elapsed = end - start
        print(f'[ Time elapsed for n = {n} ]: {elapsed}')
        return result
    return wrap_f

# Specific wrapper for fib(n) with option for units: seconds/ms
def profiling_decorator_unit(unit):
    def profiling_decorator(f):
        @wraps(f)
        def wrap_f(n):
            start = time.time()
            result = f(n)
            end = time.time()
            if unit == 'seconds':
                elapsed = (end - start) / 1000
            else:
                elapsed = (end - start)
            print(f'[ Time elapsed for n = {n} ]: {elapsed} {unit}')
            return result
        return wrap_f
    return profiling_decorator

# Decorator function that makes a class that wraps a target class and applies the decorating function 
# profiling_wrapper(f) to every method in the class and returns a new class with added functionality
def profile_class_methods(Cls):
    class ProfiledClass(object):
        def __init__(self, *args, **kwargs):
            self.inst = Cls(*args, **kwargs)
        def __getattribute__(self, s):
            try:
                x = super(ProfiledClass, self).__getattribute__(s)
            except AttributeError:
                pass
            else:
                x = self.inst.__getattribute__(s)
                if type(x) == type(self.__init__):
                    return profiling_wrapper(x)
                else:
                    return x
            return ProfiledClass



@profiling_decorator_unit('seconds')
def fib(n):
    print(f'[ Inside fib({n}) ]')
    if n < 2:
        return
    fib_prev = 1
    fib = 1
    for x in range(2, n):
        fib_prev, fib = fib, fib + fib_prev
    return fib


if __name__ == "__main__":
    n = 77
    print(f'Fibonnaci number for n = {n}: {fib(n)}')



# Reference: 
# Badenhurst, Wessel. "Chapter 7: Decorator Pattern". Practical Python Design Patterns: Pythonic Solutions to Common Problems, Apress, October 20, 2017, pp. 105-121,
# DOI: https://doi.org/10.1007/978-1-4842-2680-3_7.