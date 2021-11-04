import datetime
import os

class NameModel(object):
    def __init__(self):
        self.filename = 'notes.txt'

    def _get_append_write(self, filename):
        if os.path.exists(filename):
            return 'a'
        return 'w'

    def get_name_list(self):
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, 'r') as f:
            names = f.read().split('\n')
        return names
    
    def save_name(self, name):
        with open(self.filename, self._get_append_write(self.filename)) as f:
            f.write(f'{name}\n')
        
class TimeModel(object):
    def __init__(self):
        pass
    def get_time_of_day(self):
        time = datetime.datetime.now()
        if time.hour < 12:
            return 'morning'
        if 12 <= time.hour < 18:
            return 'afternoon'
        if time.hour >= 18:
            return 'evening'






        




# Reference: 
# Badenhurst, Wessel. "Chapter 19: Model View Controller Pattern". Practical Python Design Patterns: Pythonic Solutions to Common Problems, Apress, October 20, 2017, pp. 299-314,
# DOI: https://doi.org/10.1007/978-1-4842-2680-3_19.