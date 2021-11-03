import datetime


class Rule(object):
    def __init__(self, conditions, discounts):
        self.conditions = conditions
        self.discounts = discounts
    def evaluate(self, tab):
        if self.conditions.evaluate(tab):
            return self.discounts.calculate(tab)
        return 0
    
class Conditions(object):
    def __init__(self, expression):
        self.expression = expression
    def evaluate(self, tab):
        return self.expression.evaluate(tab)

class And(object):
    def __init__(self, expression1, expression2):
        self.expression1 = expression1
        self.expression2 = expression2
    def evaluate(self, tab):
        return self.expression1.evaluate(tab) and self.expression2.evaluate(tab)

class Or(object):
    def __init__(self, expression1, expression2):
        self.expression1 = expression1
        self.expression2 = expression2
    def evaluate(self, tab):
        return self.expression1.evaluate(tab) or self.expression2.evaluate(tab)

class PercentageDiscount(object):
    def __init__(self, item_type, percentage):
        self.item_type = item_type
        self.percentage = percentage
    def calculate(self, tab):
        if self.item_type == 'any_item':
            return  (sum([x.cost for x in tab.items]) * self.percentage / 100)
        else:
            return (sum([x.cost for x in tab.items if x.item_type == self.item_type]) * self.percentage / 100)

class CheapestFree(object):
    def __init__(self, item_type):
        self.item_type = item_type
    def calculate(self, tab):
        try:
            return min([x.cost for x in tab.items if x.item_type == self.item_type])
        except:
            return 0

class TodayIs(object):
    def __init__(self, day_of_week):
        self.day_of_week = day_of_week
    def evaluate(self, tab):
        return datetime.datetime.today().weekday() == self.day_of_week.name

class TimeIsBetween(object):
    def __init__(self, from_time, to_time):
        self.from_time = from_time
        self.to_time = to_time
    def evaluate(self, tab):
        hour_now = datetime.datetime.today().hour
        minute_now = datetime.datetime.today().minute
        from_hour, from_minute = [int(x) for x in self.from_time.split(':')]
        to_hour, to_minute = [int(x) for x in self.to_time.split(':')]
        hour_in_range = from_hour <= hour_now < to_hour
        begin_edge = hour_now == from_hour and minute_now > from_minute
        end_edge = hour_now == to_hour and minute_now < to_minute
        return any([hour_in_range, begin_edge, end_edge])

class TodayIsAWeekday(object):
    def __init__(self):
        pass
    def evaluate(self, tab):
        weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        return datetime.datetime.today().weekday() in weekdays

class TodayIsAWeekend(object):
    def __init__(self):
        pass
    def evaluate(self, tab):
        weekend = ['Saturday', 'Sunday']
        return datetime.datetime.today().weekday() in weekend

class DayoftheWeek(object):
    def __init__(self, name):
        self.name = name

class ItemIsA(object):
    def __init__(self, item_type):
        self.item_type = item_type
    def evaluate(self, item):
        return self.item_type == item.item_type

class NumberOfItemsOfType(object):
    def __init__(self, num_items, item_type):
        self.number = num_items
        self.item_type = item_type
    def evaluate(self, tab):
        return len([x for x in tab.items if x.item_type == self.item_type]) == self.number

class CustomerIsA(object):
    def __init__(self, customer_type):
        self.customer_type = customer_type
    def evaluate(self, tab):
        return tab.customer.customer_type == self.customer_type

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

class CustomerType(object):
    def __init__(self, customer_type):
        self.customer_type = customer_type


member = CustomerType('member')
pizza = ItemType('pizza')
burger = ItemType('burger')
drink = ItemType('drink')

monday = DayoftheWeek('Monday')


def setup_demo_tab():
        member_customer = Customer(member, 'John')
        tab = Tab(member_customer)
        tab.items.append(Item('Margarita', pizza, 15))
        tab.items.append(Item('Cheddar Melt', burger, 6))
        tab.items.append(Item('Hawaiian', pizza, 12))
        tab.items.append(Item('Latte', drink, 4))
        tab.items.append(Item('Club', pizza, 17))
        return tab


if __name__ == "__main__":
    
    tab = setup_demo_tab()

    rules = []
    # Members get 15% off all items
    rules.append(Rule(CustomerIsA(member), PercentageDiscount('any_item', 15)))
    # During happy hour (5-7pm weekdays) all drinks are 10% off
    rules.append(Rule(And(TimeIsBetween('17:00', '19:00'), TodayIsAWeekday()), PercentageDiscount(drink, 10)))
    # Mondays are 'buy one get one free' burger days
    rules.append(Rule(And(TodayIs(monday), NumberOfItemsOfType(burger, 2)), CheapestFree(burger)))

    for rule in rules:
        newrule = rule.evaluate(tab)
        tab.discounts.append(newrule)
    cost_before_discount = tab.calculate_cost()
    discount_applied = tab.calculate_discount()
    final_cost = cost_before_discount - discount_applied
    print(f'Customer name: {tab.customer.name}')
    print(f'Customer tyoe: {tab.customer.customer_type.customer_type}')
    print(f'Calculated cost: ${cost_before_discount:.2f}\nDiscount applied: ${discount_applied:.2f}\nTotal cost: ${final_cost:.2f}')




# Reference: 
# Badenhurst, Wessel. "Chapter 12: Interpreter Pattern". Practical Python Design Patterns: Pythonic Solutions to Common Problems, Apress, October 20, 2017, pp. 179-202,
# DOI: https://doi.org/10.1007/978-1-4842-2680-3_12.