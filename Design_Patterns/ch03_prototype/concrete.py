from prototype_1 import Prototype
from copy import deepcopy

# Declare a Concrete class that inherits from the Prototype abstract base class
class Concrete(Prototype):
    def clone(self):
        # make a deep copy of self
        return deepcopy(self)





# Reference: 
# Badenhurst, Wessel. "Chapter 3: The Prototype Pattern". Practical Python Design Patterns: Pythonic Solutions to Common Problems, Apress, October 20, 2017, pp. 37-60. 
# DOI: https://doi.org/10.1007/978-1-4842-2680-3_3