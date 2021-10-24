# Notes from Python 3.10 tutorial on Data Structures
# https://docs.python.org/3.10/tutorial/datastructures.html

# Data Structures

# Lists
print("***LISTS***\n")
"""The lists data type has several methods:
list.append(x)                  Add an item to the end of the list
list.extend(iterable)           Extend the list by appending all the items from the iterable
list.insert(i, x)               Insert item x at index i
list.remove(x)                  Remove an item from the list
list.pop([i])                   Remove the item at position i in the list, and return it (if no index specified, returns
                                the last item in the list)
list.clear()                    Remove all items from the list
list.index(x[, start[, end]])   Return 0-based index of the first item whose value is equal to x
list.count(x)                   Return number of times x appears in the list
list.sort(*, ken=None, reverse=False) Sort the items of the list in place
list.reverse()                  Reverse the elements of the list in place
list.copy()                     Return a shallow copy of the list
"""
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits)
print('Count of apple is', fruits.count('apple'))
print('Count of tangerine is', fruits.count('tangerine'))
print('Index of banana is', fruits.index('banana'))
print('Index of (banana, 4) is', fruits.index('banana', 4))
fruits.reverse()
print(fruits)
fruits.append('grape')
print(fruits)
fruits.sort()
print(fruits)
print(fruits.pop())
print()

# Using lists as stacks
print("\n***Using lists as stacks***\n")
# LIFO (last in, first out)
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print('stack: ', stack)
print('pop: ', stack.pop())
print('stack: ', stack)
print('pop: ', stack.pop())
print('pop: ', stack.pop())
print('stack: ', stack)
print()

# Using lists as queues
print("\n***Using lists as queues***\n")
# FIFO (first in, first out) with collections.deque
from collections import deque
queue = deque(['Eric', 'John', 'Michael'])
print('Queue:', queue)
queue.append('Terry')
queue.append('Graham')
print('Queue:', queue)
print('.popleft():', queue.popleft())
print('.popleft():', queue.popleft())
print('Queue:', queue)
print()

# Calculate a list of squares
squares = list(map(lambda x: x**2, range(10)))
squares2 = [x**2 for x in range(10)]
print(squares)
print(squares2)
print()

# List comprehensions
print("\n***List comprehensions***\n")
list_comp = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print(list_comp)

vec = [-4, -2, 0, 2, 4]
# create a new list with values doubled: [x*2 for x in vec]
print([x*2 for x in vec])
# filter the list to exclude negative nums: [x for x in vec if x >= 0]
print([x for x in vec if x >= 0])
# apply a function to all the elements: [abs(x) for x in vec]
print([abs(x) for x in vec])
# call a method on each element
freshfruit = ['  banana', '  loganberry', 'passion fruit  ']
print([weapon.strip() for weapon in freshfruit])
# create a list of 2-tuples like (num, square):
print([(x, x**2) for x in range(6)])
# flatten a list using a listcomp with two 'for'
vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for elem in vec for num in elem]
print(flattened)
# list comprehensions can contain complex expressions and nested functions:
from math import pi
pilist = [str(round(pi, i)) for i in range(1, 6)]
print(pilist)


# DICTIONARIES
print("\n***DICTIONARIES***\n")
"""A set of {key: value} pairs. Keys are unique within a dictionary.
Performing list(d) on a dictionary returns a list of all keys used in the dictionary, in insertion order.
You can use sorted(d) to return a list of all keys sorted."""
tel = {'jack': 4098, 'guido': 4139}
print(tel)
tel['sape'] = 4127
print(tel)
print(tel['jack'])
del tel['sape']
print(tel)
print(list(tel))
print(sorted(tel))
print(('guido' in tel))
print(('jack' not in tel))

# The dict() constructor builds dicts directly from sequences of key-value pairs:
dictionary = dict([('sape', 4139), ('guido', 4192), ('jack', 4834)])
print(dictionary)

# Dict comprehensions can be used to create dicts from arbitrary key-value pairs:
dictionary = {x: x**2 for x in (2, 4, 6)}
print(dictionary)

# When the keys are simple strings, you can specify pairs using keywords arguments:
dictionary = dict(sape=4139, guido=4327, jack=4856)
print(dictionary)


# LOOPING TECHNIQUES
print("\n***LOOPING TECHNIQUES***\n")
# When looping through dictionaries, the key-value pair can be retrieved at the same time using the items() method:
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)
print()
# When looping through a sequence, the index and value can be retrieved at the same time using the enumerate() function:
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)
print()
# To loop over 2 or more sequences, use zip() function:
questions = ['name', 'quest', 'favourite colour']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print(f'What is your {q}? It is {a}.')
print()
# To loop over a sequence in reverse, call the reversed() function:
for i in reversed(range(1, 10, 2)):
    print(i)
# You can call the sorted() function on a sequence in a loop; returns a new sorted list, leaves the original list as is:
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(basket):
    print(i)
