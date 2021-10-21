# Function like the scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print(f'arg1: {arg1}, arg2: {arg2}')


# The above *args is pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f'arg1: {arg1}, arg2: {arg2}')


# This takes just one argument
def print_one(arg1):
    print(f'arg1: {arg1}')


# This takes no arguments
def print_none():
    print("I got nothin'.")


print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()
