# basic_command.py - Allows you to queue up a string of Command() objects (a macro) for execution by an Invoker() object

# Command pattern

# When you want to send instructions from one object to another while keeoping those objects loosely coupled, one solution is to encapsulate 
# everything needed to execute the instructions in some kind of data structure. The client that initiates the execution does not have to 
# know anything about the way in which the instruction will be executed. All it is required to do is to set up all the required info and
# hand off whatever needs to happen to the next system.

# We will use an object (class) to encapsulate our instructions.  The class of objects used to encapsulate information needed by some other method in order to execute is
# called a command. The client object instantiates a command containing the method it wishes to execute, along with all the params required
# to execute the method, and some target object that has the method (the receiver). The receiver is an instance of a class that can 
# execute teh method given the encapsulated information.
 
# The command pattern can be implemented like this:


class Command:
    def __init__(self, receiver, text):
        self.receiver = receiver
        self.text = text

    def execute(self):
        self.receiver.print_message(self.text)

class Receiver(object):
    def print_message(self,text):
        print(f'Message received: {text}')

class Invoker(object):
    def __init__(self):
        self.commands = []
    def add_command(self, command):
        self.commands.append(command)
    def run(self):
        for command in self.commands:
            command.execute()

if __name__ == "__main__":
    receiver = Receiver()
    command1 = Command(receiver, 'Execute command 1')
    command2 = Command(receiver, 'Execute command 2')
    invoker = Invoker()
    invoker.add_command(command1)
    invoker.add_command(command2)
    invoker.run()



# Reference: 
# Badenhurst, Wessel. "Chapter 11: Command Pattern". Practical Python Design Patterns: Pythonic Solutions to Common Problems, Apress, October 20, 2017, pp. 167-177,
# DOI: https://doi.org/10.1007/978-1-4842-2680-3_11.