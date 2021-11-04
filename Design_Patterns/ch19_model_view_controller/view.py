class GreetingView(object):
    def __init__(self):
        pass

    def generate_greeting(self, name, time_of_day, known):
        if name == 'lion':
            print('RRRrrrrroar!')
            return
        if known:
            print(f'Good {time_of_day}. Welcome back, {name}!')
        else:
            print(f'Good {time_of_day}, {name}, nice to meet you.')








            




# Reference: 
# Badenhurst, Wessel. "Chapter 19: Model View Controller Pattern". Practical Python Design Patterns: Pythonic Solutions to Common Problems, Apress, October 20, 2017, pp. 299-314,
# DOI: https://doi.org/10.1007/978-1-4842-2680-3_19.