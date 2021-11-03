# Sample point-of-sale (POS) transaction program using the facade pattern
# We could implement a different class for each interaction, e.g. loyalty rewards, stock, specials, etc. However, if you 
# want to process a sale, you have to interact with all of these classes. This is poor systems design. The problem of 
# complex/ugly systems can be approached using the facade design pattern. This pattern is used to create a complexity-
# limiting interface to a sub-system(s).

import datetime
import random

# Invoice class:
class Invoice(object):
    def __init__(self, customer):
        pass
    
    def save(self):
        # Save the invoice to some sort of persistent storage
        pass
    
    def send_to_printer(self):
        # Send invoice representation to external printer
        pass

    def add_line(self, invoice_line):
        self.lines.append(invoice_line)
        self.calculate()
    
    def remove_line(self, line_item):
        try:
            self.lines.remove(line_item)
        except ValueError as e:
            print(f'Could not remove {line_item} because there is no such item in the invoice.')
    
    def calculate(self):
        self.total = sum(x.total * x.amount for x in self.lines)
        self.tax = sum(x.total * x.tax_rate for x in self.lines)
    
    def generate_number(self):
        rand = random.randint(1, 1000)
        return f'{self.timestamp}{rand}'


class Customer(object):
    def __init__(self):
        pass
        @classmethod
        def fetch(cls, customer_code):
            # Fetch customer from persistent storage
            pass
        def save(self):
            # Save customer to persistent storage
            pass


class Item(object):
    def __init__(self):
        pass
        @classmethod
        def fetch(cls, item_barcode):
            # Fetch item from persistent storage
            pass
        def save(self):
            # Save item to persistent storage
            pass


class Facade:
    @staticmethod
    def make_invoice(customer):
        return Invoice(customer)
    
    @staticmethod
    def make_customer(customer_id):
        return Customer(customer_id)
    
    @staticmethod
    def make_item(item_barcode):
        return Item(item_barcode)





# Reference: 
# Badenhurst, Wessel. "Chapter 8: Facade Pattern". Practical Python Design Patterns: Pythonic Solutions to Common Problems, Apress, October 20, 2017, pp. 123-132,
# DOI: https://doi.org/10.1007/978-1-4842-2680-3_8.