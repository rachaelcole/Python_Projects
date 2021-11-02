# We can use an abstract factory to create a single interface to access a collection of factory methods.
# Each abstract factory in the collection needs to implement a predefined interface, and each function
# on that interface returns another abstract type, as per the factory method pattern.

import abc
from shape_factory import Circle, Square, Shape

# Abstract factory defining the blueprint for defining concrete factories
class AbstractFactory(object):
    __metaclass__ = abc.ABCMeta
    
    @abc.abstractmethod
    def make_object(self):
        return

# Concrete factories:
class CircleFactory(AbstractFactory):
    def make_object(self):
        pass  # do something
        return Circle()

class SquareFactory(AbstractFactory):
    def make_object(self):
        pass  # do something
        return Square()

def draw_function(factory):
    drawable = factory.make_object()
    drawable.draw()

def prepare_client():
    squareFactory = SquareFactory()
    draw_function(squareFactory)
    circleFactory = CircleFactory()
    draw_function(circleFactory)





# Reference: 
# Badenhurst, Wessel. "Chapter 4: Factory Pattern". Practical Python Design Patterns: Pythonic Solutions to Common Problems, Apress, October 20, 2017, pp. 61-73,
# DOI: https://doi.org/10.1007/978-1-4842-2680-3_4. 