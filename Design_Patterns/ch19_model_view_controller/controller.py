# A name/greeting program using the generic controller, model, and view objects

import sys
from model import *
from view import GreetingView

class GreetingController(object):
    def __init__(self):
        self.name_model = NameModel()
        self.time_model = TimeModel()
        self.view = GreetingView()
    
    def handle(self, request):
        if request in self.name_model.get_name_list():
            self.view.generate_greeting(name=request, time_of_day=self.time_model.get_time_of_day(), known=True)
        else:
            self.name_model.save_name(request)
            self.view.generate_greeting(name=request, time_of_day=self.time_model.get_time_of_day(), known=False)
    

def main(name):
    request_handler = GreetingController()
    request_handler.handle(name)

if __name__ == "__main__":
    main(sys.argv[1])
    








# Reference: 
# Badenhurst, Wessel. "Chapter 19: Model View Controller Pattern". Practical Python Design Patterns: Pythonic Solutions to Common Problems, Apress, October 20, 2017, pp. 299-314,
# DOI: https://doi.org/10.1007/978-1-4842-2680-3_19.