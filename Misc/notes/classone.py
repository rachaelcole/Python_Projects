class Calculator(object):
    # Define class to simulate a simple calculator; __init__ creates/initialises an instance of the Class
    def __init__(self):
        # Start with zero
        self.current = 0

    def add(self, amount):
        # Add number to current
        self.current += amount

    def get_current(self):
        return self.current


myBuddy = Calculator()  # make myBuddy into a Calculator object
myBuddy.add(2)  # use myBuddy's add() method derived from the Calculator class
print(myBuddy.get_current())  # print myBuddy's current instance variable
