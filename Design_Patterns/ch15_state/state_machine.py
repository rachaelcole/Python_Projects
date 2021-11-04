# State pattern

# State diagrams are a visual representation of the states of a program/system given certain inputs. A state machine is useful in 
# modeling the state of an object and the things that cause the object to change states. The state pattern is used to encapsulate
# behaviour variations based on the internal state of the object.

# Define an empty base class that the concrete State classes can inherit from:
class State(object):
    pass

# n.b. these concrete states lack action methods for this sample implementation
class ConcreteState1(State):
    def __init__(self, state_machine):
        self.state_machine = state_machine
    def switch_state(self):
        self.state_machine.state = self.state_machine.state2

class ConcreteState2(State):
    def __init__(self, state_machine):
        self.state_machine = state_machine
    def switch_state(self):
        self.state_machine.state = self.state_machine.state1

class StateMachine(object):
    def __init__(self):
        self.state1 = ConcreteState1(self)
        self.state2 = ConcreteState2(self)
        self.state = self.state1
    def switch(self):
        self.state.switch_state()
    def __str__(self):
        return str(self.state)

def main():
    state_machine = StateMachine()
    print(state_machine)
    state_machine.switch()
    print(state_machine)

if __name__ == "__main__":
    main()





# Reference: 
# Badenhurst, Wessel. "Chapter 15: State Pattern". Practical Python Design Patterns: Pythonic Solutions to Common Problems, Apress, October 20, 2017, pp. 239-248,
# DOI: https://doi.org/10.1007/978-1-4842-2680-3_15.