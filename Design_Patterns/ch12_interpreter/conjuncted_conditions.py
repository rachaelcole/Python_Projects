# Conditions can be a set of conjuncted conditions, or a set of disjuncted conditions, or a single Boolean expression


class AndConditions(object):
    def __init__(self):
        self.conditions = []
    def evaluate(self, tab):
        return all(x.evaluate(tab) for x in self.conditions)
    def add(self, condition):
        self.conditions.append(condition)
    def remove(self, condition):
        self.conditions.remove(condition)

class OrConditions(object):
    def __init__(self):
        self.conditions = []
    def evaluate(self, tab):
        return any(x.evaluate(tab) for x in self.conditions)
    def add(self, condition):
        self.conditions.append(condition)
    def remove(self, condition):
        self.conditions.remove(condition)

class Condition(object):
    def __init__(self, condition_function):
        self.test = condition_function
    def evaluate(self, tab):
        return self.test(tab)

class Discounts(object):
    def __init__(self):
        self.children = []
    def calculate(self, tab):
        return sum(x.calculate(tab) for x in self.children)
    def add(self, child):
        self.children.append(child)
    def remove(self, child):
        self.children.remove(child)

class Discount(object):
    def __init__(self, test_function, discount_function):
        self.test = test_function
        self.discount = discount_function
    def calculate(self, tab):
        return sum(self.discount(item) for item in tab.items if self.test(item))

class Rule(object):
    def __init__(self, tab):
        self.tab = tab
        self.conditions = AndConditions()
        self.discounts = Discounts()
    def add_conditions(self, conditions):
        self.conditions.add(conditions)
    def add_discount(self, test_function, discount_function):
        discount = Discount(test_function, discount_function)
        self.discounts.add(discount)
    def apply(self):
        if self.conditions.evaluate(self.tab):
            return self.discounts.calculate(self.tab)
        return 0






# Reference: 
# Badenhurst, Wessel. "Chapter 12: Interpreter Pattern". Practical Python Design Patterns: Pythonic Solutions to Common Problems, Apress, October 20, 2017, pp. 179-202,
# DOI: https://doi.org/10.1007/978-1-4842-2680-3_12.