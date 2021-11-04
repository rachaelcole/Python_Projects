# Generator functions

# Generators are a great way to simplify the creation of iterators since a generator is a function that produces a sequence
# of results and follows the interface ffoctions that can be iterated over as per the Python iterator pattern. When a generator
# function is called, it returns a generator object but doesn't begin any execution until the __next__() method is called. The
# generator returned by the generator function is also an iterator.

def gen_squares(n):  # Every time you call this function the output changes
    i = 0
    while i < n:
        # The function starts executing after the yield statement and continues until it hits yield again
        yield i*i    # Keep a record of the current state of the function and return the value that is yielded
        print('next i')
        i += 1


if __name__ == "__main__":
    # We can re-write the above function using a generator expression, which is similar to a list comprehension: g = (x*x for x in range(n))
    g = (x*x for x in range(4))
    print(g.__next__())
    print(g.__next__())
    print(g.__next__())
    print(g.__next__())
    print(g.__next__())


# Reference: 
# Badenhurst, Wessel. "Chapter 13: Iterator Pattern". Practical Python Design Patterns: Pythonic Solutions to Common Problems, Apress, October 20, 2017, pp. 203-217,
# DOI: https://doi.org/10.1007/978-1-4842-2680-3_13.