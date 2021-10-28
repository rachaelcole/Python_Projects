from math import isclose
from random import uniform, random, randint
from numpy import dtype
from vectors import *
from classes import *
from matrices import *
from datetime import datetime, timedelta
from json import loads, dumps
from pathlib import Path
from tests import *

# We can think of each instance of this class as a vector
class CarForSale(Vector):
    retrieved_date = datetime(2021,10,12,12)  # date of data retrieval
    def __init__(self, model_year, mileage, price, posted_datetime, model="(virtual)", source="(virtual)", location="(virtual)", description="(virtual)"):
        self.model_year = model_year
        self.mileage = mileage
        self.price = price
        self.posted_datetime = posted_datetime
        self.model = model
        self.source = source
        self.location = location
        self.description = description
    def add(self, other):
        def add_dates(d1, d2):  # helper function adds dates by adding the time spanned from the retrieved_date
            age1 = CarForSale.retrieved_date - d1
            age2 = CarForSale.retrieved_date - d2
            sum_age = age1 + age2
            return CarForSale.retrieved_date - sum_age
        return CarForSale(
            self.model_year + other.model_year,
            self.mileage + other.mileage,
            self.price + other.price,
            add_dates(self.posted_datetime, other.posted_datetime)
            )
    def scale(self, scalar):
        def scale_date(d):
            age = CarForSale.retrieved_date - d
            return CarForSale.retrieved_date - (scalar * age)
        return CarForSale(
            scalar * self.model_year,
            scalar * self.mileage,
            scalar * self.price,
            scale_date(self.posted_datetime)
        )
    @classmethod
    def zero(cls):
        return CarForSale(0, 0, 0, CarForSale.retrieved_date)


# Load JSON car data
contents = Path('cargraph.json').read_text()
cg = loads(contents)
cleaned = []

# Clean the data
def parse_date(s):
    input_format = "%m/%d - %H:%M"
    dt = datetime.strptime(s, input_format).replace(year=2021)
    return dt

for car in cg[1:]:
    try:
        row = CarForSale(int(car[1]), float(car[3]), float(car[4]), parse_date(car[6]), car[2], car[5], car[7], car[8])
        cleaned.append(row)
    except:
        pass

cars = cleaned 

# print((cars[0] + cars[1]).__dict__)

average_prius = sum(cars, CarForSale.zero()) * (1.0/len(cars))
# print(average_prius.__dict__)



### TESTING ###

# Generate random data and make equality tests for them 
def random_time():
    return CarForSale.retrieved_date - timedelta(days=uniform(0,10))

def approx_equal_time(t1, t2):
    test = datetime.now()
    return isclose((test - t1).total_seconds(), (test - t2).total_seconds())

def random_car():
    return CarForSale(randint(1990,2021), randint(0,250000), 27000. * random(), random_time())

def approx_equal_car(c1, c2):
    return (isclose(c1.model_year, c2.model_year)
    and isclose(c1.mileage, c2.mileage)
    and isclose(c1.price, c2.price)
    and approx_equal_time(c1.posted_datetime, c2.posted_datetime))

# Run the tests:
for i in range(0,100):
    a, b = random_scalar(), random_scalar()
    u, v, w = random_car(), random_car(), random_car()
    test(CarForSale.zero(), approx_equal_car, a,b,u,v,w)