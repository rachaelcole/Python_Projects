# A program using the generic controller, model, and view objects

import sys

class GenericController(object):
    def __init__(self):
        self.model = GenericModel()
        self.view = GenericView()
    
    def handle(self, request):
        data = self.model.get_data(request)
        self.view.generate_response(data)


class GenericModel(object):
    def __init__(self):
        pass

    def get_data(self, request):
        return {'request': request}


class GenericView(object):
    def __init__(self):
        pass

    def generate_response(self, data):
        print(data)


def main(name):
    request_handler = GenericController()
    request_handler.handle(name)


if __name__ == "__main__":
    main(sys.argv[1])


# Reference: 
# Badenhurst, Wessel. "Chapter 19: Model View Controller Pattern". Practical Python Design Patterns: Pythonic Solutions to Common Problems, Apress, October 20, 2017, pp. 299-314,
# DOI: https://doi.org/10.1007/978-1-4842-2680-3_19.