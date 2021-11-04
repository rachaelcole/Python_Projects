# Strategy pattern
# Suppose you want to reduce two values to a single value. A simple solution could look like this:

def reducer(arg1, arg2, strategy=None):
    """Reduces two numeric values to one numeric value using different strategies."""
    # The problem with this implementation is that every time you want to add a strategy, you have to add another elif block to
    # this function. We would prefer a modular solution that allows us to pass in new strategies without having to alter the
    # code that uses or executes the strategy.
    if strategy == 'addition':
        print(arg1 + arg2)
    elif strategy == 'subtraction':
        print(arg1 - arg2)
    else:
        print('Strategy not implemented')


def main():
    reducer(4,6)
    reducer(4,6,'addition')
    reducer(4,6,'subtraction')


if __name__ == "__main__":
    main()




# Reference: 
# Badenhurst, Wessel. "Chapter 16: Strategy Pattern". Practical Python Design Patterns: Pythonic Solutions to Common Problems, Apress, October 20, 2017, pp. 249-255,
# DOI: https://doi.org/10.1007/978-1-4842-2680-3_16.