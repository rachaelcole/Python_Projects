# We can improve the code in reducer.py using the strategy design pattern, which allows us to write code that uses some strategy
# to be selected at runtime without knowing anything about the strategy other than it follows some execution signature. We can use
# objects (classes) to implement the strategy pattern.

# StrategyExecutor() object with an execute method that calls the execute method of the strategy object
class StrategyExecutor(object):
    def __init__(self, strategy=None):
        self.strategy = strategy
    
    def execute(self, arg1, arg2):
        if self.strategy is None:
            print('Error: Strategy not implemented')
        else:
            self.strategy.execute(arg1, arg2)

# Each strategy is an object with an execute(x,y) method
class AdditionStrategy(object):
    def execute(self, arg1, arg2):
        print(arg1 + arg2)

class SubtractionStrategy(object):
    def execute(self, arg1, arg2):
        print(arg1 - arg2)

# Main program execution:
def main():
    # Calling the StrategyExecutor() object without passing in a strategy object as a parameter
    no_strategy = StrategyExecutor()
    # Calling the StrategyExecutor() object with strategy objects as parameters
    addition_strategy = StrategyExecutor(AdditionStrategy())
    subtraction_strategy = StrategyExecutor(SubtractionStrategy())

    # Calling the .execute() method on our new object variables
    no_strategy.execute(4, 6)           # >> 'Error: Strategy not implemented'
    addition_strategy.execute(4, 6)     # >> 10
    subtraction_strategy.execute(4, 6)  # >> -2


if __name__ == "__main__":
    main()  # Execute the program






# Reference: 
# Badenhurst, Wessel. "Chapter 16: Strategy Pattern". Practical Python Design Patterns: Pythonic Solutions to Common Problems, Apress, October 20, 2017, pp. 249-255,
# DOI: https://doi.org/10.1007/978-1-4842-2680-3_16.