from classes import *
from random import uniform, random, randint  # Used for unit testing function random_scalar()
from math import isclose  # Checks two float values don't differ by a significant amount
from vectors import *
from matrices import *
from datetime import datetime, timedelta

### TESTING VECTOR() OBJECTS ###
# Example unit test:
s = -3
u, v = Vec2(42, -10), Vec2(1.5, 8)
# print(s * (u + v) == s * v + s * u)  # >> returns True, proving a * (v + w) == a*v + a*w


# Improved unit test written as functions to generate random tests of the rule:
def random_scalar():
    return uniform(-10, 10)

def random_vec2():
    return Vec2(random_scalar(), random_scalar())

# Adding necessary functions for using our generalised test() function to test Vec3 objects:
def random_vec3():
    return Vec3(random_scalar(), random_scalar(), random_scalar())

def approx_equal_vec3(v, w):
    return isclose(v.x,w.x) and isclose(v.y,w.y) and isclose(v.z,w.z)

# Function that ignores tiny discrepancies using math.isclose():
def approx_equal_vec2(v,w):
    return isclose(v.x, w.x) and isclose(v.y, w.y)  # Tests whether the x and y components are close

# TEST EXAMPLE:
# for _ in range(0,100):  # Run the test for 100 different randomly-generated scalars and pairs of vectors
#     a = random_scalar()
#     u, v = random_vec2(), random_vec2()
#     assert approx_equal_vec2(a * (u+v), a*v + a*u)  # Replaces a strict equality check with the new function

# Improving our testing further:
def test(zero,eq, a, b, u, v, w):  # Pass in the zero function as 'zero' and the equality test function as 'eq'
    assert eq(u + v, v + u)
    assert eq(u + (v + w), (u + v) + w)
    assert eq(a * (b * v), (a * b) * v)
    assert eq(1 * v, v)
    assert eq((a + b) * v, a * v + b * v)
    assert eq(a * v + a * w, a * (v + w))
    # Checking against the zero() vector
    assert eq(zero + v, v)
    assert eq(0 * v, zero)
    assert eq(-v + v, zero)


# Testing 2D vectors with .zero() method
# for i in range(0,100):
#     a,b = random_scalar(), random_scalar()
#     u,v,w = random_vec2(), random_vec2(), random_vec2()
#     test(Vec2.zero(), approx_equal_vec2, a,b,u,v,w)

# Running the vector space unit tests with float values for u, v and w:
# for i in range(0, 100):
#     a, b = random_scalar(), random_scalar()
#     u, v, w = random_scalar(), random_scalar(), random_scalar()
#     test(0, isclose, a, b, u, v, w)


### TESTING CARFORSALE() OBJECTS ###

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


# Test whether two functions are equal
def approx_equal_function(f,g):
    results = []
    for _ in range(0, 10):
        x = uniform(-10,10)
        results.append(isclose(f(x),g(x)))
    return all(results)


# Get a random Polynomial function
def random_function():
    degree = randint(0,5)
    p = Polynomial(*[uniform(-10, 10) for _ in range(0, degree)])
    return Function(lambda x: p(x))


# Unit testing for 5x3 matrixes

# Define funcs for random inputs:
def random_matrix(rows, columns):
    return tuple(
        tuple(uniform(-10,10) for j in range(0,columns))
        for i in range(0, rows))

def random_5_by_3():
    return Matrix5_by_3(random_matrix(5,3))

def approx_equal_matrix_5_by_3(m1,m2):
    return all([
        isclose(m1.matrix[i][j], m2.matrix[i][j])
        for j in range(0,3) for i in range(0,5)])

# Run the test
"""
for i in range(0,100):
    a,b = random_scalar(), random_scalar()
    u,v,w = random_5_by_3(), random_5_by_3(), random_5_by_3()
    test(Matrix5_by_3.zero(), approx_equal_matrix_5_by_3, a,b,u,v,w)
"""