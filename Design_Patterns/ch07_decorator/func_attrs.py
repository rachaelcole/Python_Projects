# Ideally, we don't want the function using a decorator to be changed in any way but the way we intend. However,
# in our previous example in func_decorated_fib.py, the __name__ and __doc__ attributes of the original fib(n)
# function are overwritten by the wrapper.

# We can alter the func_decorated_fib.py decorator function to retain the __name__ and __doc__ attributes
# of the original function throughout decoration. Python has a module called functools for this.

from functools import wraps

def dummy_decorator(f):
    @wraps(f)  # Keeps the original function's __name__ and __doc__ attributes persistent through wrapping
    def wrap_f():
        print(f'Function to be decorated: {f.__name__}')
        print(f'Nested wrapping function: {wrap_f.__name__}')
        return f()
    return wrap_f()

@dummy_decorator
def do_nothing():
    print('Inside "do_nothing()"')


if __name__ == "__main__":
    print(f'Wrapped function: {do_nothing.__name__}')
    do_nothing()



    

# Reference: 
# Badenhurst, Wessel. "Chapter 7: Decorator Pattern". Practical Python Design Patterns: Pythonic Solutions to Common Problems, Apress, October 20, 2017, pp. 105-121,
# DOI: https://doi.org/10.1007/978-1-4842-2680-3_7.