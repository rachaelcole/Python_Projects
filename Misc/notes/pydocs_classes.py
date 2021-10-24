# Notes from Python 3.10 tutorial on Classes
# https://docs.python.org/3.10/tutorial/classes.html#tut-classes

"""
CLASSES

Classes provide a way of bundling data and functionality together.
Creating a new class creates a new type of object. You can make instances of that type.
Each class instance can have attributes and methods.
Class inheritance allows multiple base classes, a derived class can override any methods of its base class(es), and a
method can call the method of a base class with the same name.
A NAMESPACE is a mapping from names to objects.
A SCOPE is a textual region of a Python program where a namespace is directly accessible.
"""

print('***SCOPE***\n')

# Scope example
def scope_test():
    def do_local():
        spam = 'local spam'

    def do_nonlocal():
        nonlocal spam
        spam = 'nonlocal spam'

    def do_global():
        global spam
        spam = 'global spam'

    spam = 'test spam'
    do_local()
    print(f'After local assignment: {spam}')
    do_nonlocal()
    print(f'After nonlocal assignment: {spam}')
    do_global()
    print(f'After global assignment: {spam}')

scope_test()
print('In global scope:', spam)


print('\n***CLASS SYNTAX***\n')
print("""The simplest form of class definition:

class Classname:
    <statement-1>
    .
    .
    .
    <statement-N>""")


class MyClass:
    """A simple example class."""
    i = 12345

    def __init__(self):
        self.data = []

    def f(self):
        return 'hello world'

x = MyClass()
print(x.f())

class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

x = Complex(3.0, -4.5)
print(x.r, ',', x.i)
