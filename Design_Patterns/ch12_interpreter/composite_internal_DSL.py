# Implementation of an example pizza shop's discount rule as a rudimentary internal DSL (domain-specific language)

class Tab(object):
    def __init__(self, customer):
        self.items = []
        self.discounts = []
        self.customer = customer
    def calculate_cost(self):
        return sum(x.cost for x in self.items)
    def calculate_discount(self):
        return sum(x for x in self.discounts)

class Item(object):
    def __init__(self, name, item_type, cost):
        self.name = name
        self.item_type = item_type
        self.cost = cost

class ItemType(object):
    def __init__(self, name):
        self.name = name

class Customer(object):
    def __init__(self, customer_type, name):
        self.customer_type = customer_type
        self.name = name

    def is_a(self, customer_type):
        return self.customer_type == customer_type

class Discount(object):
    def __init__(self, amount):
        self.amount = amount

class CustomerType(object):
    def __init__(self, customer_type):
        self.customer_type = customer_type
    

class Rule(object):
    def __init__(self, tab):
        self.tab = tab
        self.conditions = []
        self.discounts = []
    def add_condition(self, test_value):
        self.conditions.append(test_value)
    def add_percentage_discount(self, item_type, percent):
        if item_type == 'any item':
            f = lambda x: True
        else:
            f = lambda x: x.item_type == item_type
        items_to_discount = [item for item in self.tab.items if f(item)]
        for item in items_to_discount:
            discount = Discount(item.cost * (percent/100.0))
            self.discounts.append(discount)
    def apply(self):
        if all(self.conditions):
            return sum(x.amount for x in self.discounts)
        return 0



if __name__ == "__main__":
    member = CustomerType('Member')
    member_customer = Customer(member, 'John')
    tab = Tab(member_customer)

    pizza = ItemType('pizza')
    burger = ItemType('burger')
    drink = ItemType('drink')

    tab.items.append(Item('Margarita', pizza, 15))
    tab.items.append(Item('Cheddar Melt', burger, 6))
    tab.items.append(Item('Latte', drink, 4))
    
    rule = Rule(tab)
    rule.add_condition(tab.customer.is_a(member))
    rule.add_percentage_discount('any item', 15)

    tab.discounts.append(rule.apply())

    print(f'Calculated cost: {tab.calculate_cost()}\nDiscount applied: {tab.calculate_discount()}\n{100 * tab.calculate_discount() / tab.calculate_cost()}% Discount applied.')





# Reference: 
# Badenhurst, Wessel. "Chapter 12: Interpreter Pattern". Practical Python Design Patterns: Pythonic Solutions to Common Problems, Apress, October 20, 2017, pp. 179-202,
# DOI: https://doi.org/10.1007/978-1-4842-2680-3_12.