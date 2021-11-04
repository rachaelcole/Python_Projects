# We can improve the code in strategy_pattern.py by passing strategy functions to the StrategyExecutor() class without first wrapping the
# functions in their own classes. This makes the code easier to read and test.

# StrategyExecutor(strategy_function) object with a default execute method (that can be overwritten at invocation by calling a strategy func
# as an argument when you invoke the StrategyExecutor() object)
class StrategyExecutor(object):
    def __init__(self, func=None):
        if func is not None:
            self.execute = func
    
    def execute(self, *args):
        return 'Error: Strategy not implemented'

# The above object can be discarded and replaced with a function for a more elegant solution:
def executor(arg1, arg2, func=None):
    if func is None:
        return 'Error: Strategy not implemented'
    return func(arg1, arg2)


# Each strategy is a function that can be passed to the StrategyExecutor() object as an argument
def strategy_addition(arg1, arg2):
    return arg1 + arg2

def strategy_subtraction(arg1, arg2):
    return arg1 - arg2

# Main program execution:
def main():
    # Calling the StrategyExecutor() object without passing in a strategy object as a parameter
    no_strategy = StrategyExecutor()
    # Calling the StrategyExecutor() object with strategy objects as parameters
    addition_strategy = StrategyExecutor(strategy_addition)
    subtraction_strategy = StrategyExecutor(strategy_subtraction)

    # Calling the .execute() method on our new object variables
    no_strategy.execute(4, 6)           # >> 'Error: Strategy not implemented'
    addition_strategy.execute(4, 6)     # >> 10
    subtraction_strategy.execute(4, 6)  # >> -2

    # Calling the executor() function (same output as above)
    executor(4,6)
    executor(4,6,strategy_addition)
    executor(4,6,strategy_subtraction)


if __name__ == "__main__":
    main()  # Execute the program






# Reference: 
# Badenhurst, Wessel. "Chapter 16: Strategy Pattern". Practical Python Design Patterns: Pythonic Solutions to Common Problems, Apress, October 20, 2017, pp. 249-255,
# DOI: https://doi.org/10.1007/978-1-4842-2680-3_16.