# Model view controller pattern
# Using a command-line dummy program, we will demonstrate the model view controller design pattern. Our first program takes 
# a name as an argument. If the name is already stored, a welcome message is printed. Otherwise, a nice to meet you message
# is printed.

import sys
import os

def get_append_write(filename):
    if os.path.exists(filename):
        return 'a'
    return 'w'

def name_in_file(filename, name):
    if not os.path.exists(filename):
        return False
    return name in read_names(filename)

def read_names(filename):
    with open(filename, 'r') as f:
        names = f.read().split('\n')
    return names

def write_name(filename, name):
    with open(filename, get_append_write(filename)) as f:
        f.write(f'{name}\n')

def get_message(filename, name):
    if name == 'lion':
        return 'RRRrrrrroar!'
    if name_in_file(filename, name):
        return f'Welcome back, {name}!'
    write_name(filename, name)
    return f'Hi, {name}, nice to meet you.'

def main(name): 
    print(get_message('names.txt', name))

if __name__ == "__main__":
    main(sys.argv[1])



# Reference: 
# Badenhurst, Wessel. "Chapter 19: Model View Controller Pattern". Practical Python Design Patterns: Pythonic Solutions to Common Problems, Apress, October 20, 2017, pp. 299-314,
# DOI: https://doi.org/10.1007/978-1-4842-2680-3_19.