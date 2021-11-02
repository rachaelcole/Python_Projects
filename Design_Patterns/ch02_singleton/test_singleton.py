from singleton_object import SingletonObject

obj1 = SingletonObject()

obj1.val = "Object value 1"
print("Print obj: ", obj1)

print("-----")

obj2 = SingletonObject()
obj2.val = "Object value 2"
print("Print obj1: ", obj1)
print("Print obj2: ", obj2)





# Reference: 
# Badenhurst, Wessel. "Chapter 2: The Singleton Pattern". Practical Python Design Patterns: Pythonic Solutions to Common Problems, Apress, October 20, 2017, pp. 23-36. 
# DOI: https://doi.org/10.1007/978-1-4842-2680-3_2