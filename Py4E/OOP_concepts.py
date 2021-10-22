# Object-Oriented Programming
# Reference: https://www.py4e.com/html3/14-objects

stuff = list()                      # Constructs an object of type list
stuff.append('rachael')             # Call the append() method
stuff.append('python')
stuff.append('chuck')
stuff.sort()                        # Call the sort() method
print(stuff[0])                     # Retrieve the item at index 0
print(stuff.__getitem__(0))         # Call the __getitem__() method in the stuff list with a parameter of 0
print(list.__getitem__(stuff, 0))   # Call the __getitem__() method in the list object with parameters of stuff and 0
print(dir(stuff))                   # Prints all the capabilities of the stuff object (its methods)


class PartyAnimal:
    x = 0                               # attribute

    def __init__(self):                 # init method; called a 'constructor'
        print('I am constructed.')

    def party(self):                    # method
        self.x = self.x + 1
        print(f'So far: {self.x}')

    def __del__(self):                  # delete method
        print('I am destroyed', self.x)


an = PartyAnimal()                      # constructs an object called 'an' that is an instance of the PartyAnimal class
an.party()                              # calls the party() method
an.party()
an.party()
PartyAnimal.party(an)                   # another way of calling the party() method

print(f'Type of \'an\': {type(an)}')            # Returns: <class '__main__.PartyAnimal'>
print(f'Dir of \'an\': {dir(an)}')              # Returns: ['__class__', '__delattr__', '__dict__', ..., 'party', 'x' ]
print(f'Type of \'x\': {type(an.x)}')           # Returns: <class 'int'>
print(f'Type of \'party\': {type(an.party)}')   # Returns: <class 'method'>


an = 42                              # destroys previous 'an' object, and reuses the 'an' var. to store the value of 42
print(f'"an" contains {an}')
