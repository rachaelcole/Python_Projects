# calculator.py - A basic calculator built using the command design pattern

class AddCommand(object):
    def __init__(self, receiver, value):
        self.receiver = receiver
        self.value = value
    def execute(self):
        self.receiver.add(self.value)
    def undo(self):
        self.receiver.subtract(self.value)

class SubtractCommand(object):
    def __init__(self, receiver, value):
        self.receiver = receiver
        self.value = value
    def execute(self):
        self.receiver.subtract(self.value)
    def undo(self):
        self.receiver.add(self.value)

class MultiplyCommand(object):
    def __init__(self, receiver, value):
        self.receiver = receiver
        self.value = value
    def execute(self):
        self.receiver.multiply(self.value)
    def undo(self):
        self.receiver.divide(self.value)

class DivideCommand(object):
    def __init__(self, receiver, value):
        self.receiver = receiver
        self.value = value
    def execute(self):
        self.receiver.divide(self.value)
    def undo(self):
        self.receiver.multiply(self.value)

class CalculationInvoker(object):
    def __init__(self):
        self.commands = []
        self.undo_stack = []
    def add_new_command(self, command):
        self.commands.append(command)
    def run(self):
        for command in self.commands:
            command.execute()
            self.undo_stack.append(command)
    def undo(self):
        undo_command = self.undo_stack.pop()
        undo_command.undo()

class Accumulator(object):
    def __init__(self, value):
        self._value = value
    def add(self, value):
        self._value += value
    def subtract(self, value):
        self._value -= value
    def multiply(self, value):
        self._value *= value
    def divide(self, value):
        self._value /= value
    def __str__(self):
        return f'Current value: {self._value}'


if __name__ == "__main__":
    acc = Accumulator(10.0)

    invoker = CalculationInvoker()
    invoker.add_new_command(AddCommand(acc, 11))
    invoker.add_new_command(SubtractCommand(acc, 12))
    invoker.add_new_command(MultiplyCommand(acc, 13))
    invoker.add_new_command(DivideCommand(acc, 14))

    invoker.run()

    print(acc)

    for i in range(0,4):
        invoker.undo()

    print(acc)


# Reference: 
# Badenhurst, Wessel. "Chapter 11: Command Pattern". Practical Python Design Patterns: Pythonic Solutions to Common Problems, Apress, October 20, 2017, pp. 167-177,
# DOI: https://doi.org/10.1007/978-1-4842-2680-3_11.