# We want to create an interface that a collection data type can inherit, which would allow it to generalise the action
# of traversing the contents of the collection. We can do this as follows:
    # First, define an interface that defines a function that gets the next item in the collection, and another function
    # to alert some external function that there are no more elements left in the collection to return
    # Second, define an object that can use the interface to traverse the collection (the iterator)

import abc

class Iterator(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def has_next(self): pass

    @abc.abstractmethod
    def next(self): pass


class Container(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def getIterator(self): pass


class MyListIterator(Iterator):
    def __init__(self, my_list):
        self.index = 0
        self.list = my_list.list
    
    def has_next(self):
        return self.index < len(self.list)
    
    def next(self):
        self.index += 1
        return self.list[self.index - 1]

class MyList(Container):
    def __init__(self, *args):
        self.list = list(args)
    
    def getIterator(self):
        return MyListIterator(self)

if __name__ == "__main__":
    my_list = MyList(1,2,3,4,5,6)
    my_iterator = my_list.getIterator()

    while my_iterator.has_next():
        print(my_iterator.next())





# Reference: 
# Badenhurst, Wessel. "Chapter 13: Iterator Pattern". Practical Python Design Patterns: Pythonic Solutions to Common Problems, Apress, October 20, 2017, pp. 203-217,
# DOI: https://doi.org/10.1007/978-1-4842-2680-3_13.