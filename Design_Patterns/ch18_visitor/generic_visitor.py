# A generic implementation of the visitor pattern
import abc

class Visitable(object):
    def accept(self, visitor):
        visitor.visit(self)

class CompositeVisitable(Visitable):
    def __init__(self, iterable):
        self.iterable = iterable

    def accept(self, visitor):
        for element in self.iterable:
            element.accept(visitor)
        visitor.visit(self)

class AbstractVisitor(object):
    __metaclass__ = abc.ABCMeta
    @abc.abstractmethod
    def visit(self, element):
        raise NotImplementedError('A visitor needs to define a visit method')

class ConcreteVisitable(Visitable):
    def __init__(self):
        pass

class ConcreteVisitor(AbstractVisitor):
    def visit(self, element):
        pass





# Reference: 
# Badenhurst, Wessel. "Chapter 18: Visitor Pattern". Practical Python Design Patterns: Pythonic Solutions to Common Problems, Apress, October 20, 2017, pp. 271-297,
# DOI: https://doi.org/10.1007/978-1-4842-2680-3_18.