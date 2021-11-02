from abc import ABCMeta, abstractmethod

# Declare an abstract base class that specifies a clone() abstract method
class Prototype(metaclass=ABCMeta):
    @abstractmethod
    def clone():
        pass







# Reference: 
# Badenhurst, Wessel. "Chapter 3: The Prototype Pattern". Practical Python Design Patterns: Pythonic Solutions to Common Problems, Apress, October 20, 2017, pp. 37-60. 
# DOI: https://doi.org/10.1007/978-1-4842-2680-3_3