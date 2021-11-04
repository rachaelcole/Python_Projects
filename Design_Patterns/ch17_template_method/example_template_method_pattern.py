# Template Method pattern

# The template method provides a method template that can be followed to implement a specific process step by step, and then that
# template can be used in many different scenarios with minor changes. It would look like this when implemented:

import abc

class TemplateAbstractBaseClass(metaclass=abc.ABCMeta):
    # Method used to execute the process
    def template_method(self):
        self._step_1()
        self._step_2()
        self._step_3()
    
    @abc.abstractmethod
    def _step_1(self): pass
    
    @abc.abstractmethod
    def _step_2(self): pass

    @abc.abstractmethod
    def _step_3(self):pass


class ConcreteImplementationClass(TemplateAbstractBaseClass):
    def _step_1(self): pass
    def _step_2(self): pass
    def _step_3(self): pass


# Reference: 
# Badenhurst, Wessel. "Chapter 17: Template Method Pattern". Practical Python Design Patterns: Pythonic Solutions to Common Problems, Apress, October 20, 2017, pp. 257-270,
# DOI: https://doi.org/10.1007/978-1-4842-2680-3_17.