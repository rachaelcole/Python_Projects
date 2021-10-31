import numpy as np
from math import exp, e
import matplotlib.pyplot as plt
from vectors import length
from car_data import priuses

# Extract mileage/price from car_data
prius_mileage_price = [(p.mileage, p.price) for p in priuses]

# Helper functions (all from ch12 cannonball.py):
def plot_function(f,xmin,xmax,**kwargs):
    ts = np.linspace(xmin,xmax,1000)
    plt.plot(ts,[f(t) for t in ts],**kwargs)

def scalar_field_heatmap(f, xmin, xmax, ymin, ymax, xsteps=100, ysteps=100):
    fig = plt.figure()
    fig.set_size_inches(7,7)
    fv = np.vectorize(f)
    X = np.linspace(xmin, xmax, xsteps)
    Y = np.linspace(ymin, ymax, ysteps)
    X, Y = np.meshgrid(X, Y)
    z = fv(X,Y)
    fig,ax = plt.subplots()
    c = ax.pcolormesh(X,Y,z,cmap='plasma')
    ax.axis([X.min(), X.max(), Y.min(), Y.max()])
    fig.colorbar(c, ax=ax)

def secant_slope(f, xmin, xmax):
    return (f(xmax) - f(xmin)) / (xmax - xmin)

def approx_derivative(f, x, dx=1e-6):
    return secant_slope(f, x-dx, x+dx)

def approx_gradient(f, x0, y0, dx=1e-6):
    partial_x = approx_derivative(lambda x: f(x, y0), x0, dx=dx)
    partial_y = approx_derivative(lambda y: f(x0, y), y0, dx=dx)
    return (partial_x, partial_y)

def gradient_descent(f, xstart, ystart, tolerance=1e-6):
    x = xstart
    y = ystart
    grad = approx_gradient(f,x,y)
    while length(grad) > tolerance:
        x -= grad[0]
        y -= grad[1]
        grad = approx_gradient(f, x, y)
    return x, y

# New helper functions from ch14:
def draw_cost(h,points):
    xs = [t[0] for t in points]
    ys = [t[1] for t in points]
    plt.scatter(xs,ys)
    plot_function(h,min(xs),max(xs),c='k')
    for (x,y) in points:
        plt.plot([x,x],[y,h(x)],c='r')

def draw_square_cost(h,points):
    xs = [t[0] for t in points]
    ys = [t[1] for t in points]
    plt.scatter(xs,ys)
    plot_function(h,min(xs),max(xs),c='k')
    for (x,y) in points:
        e = abs(y - h(x))
        plt.plot([x,x],[y,h(x)],c='r')
        plt.fill([x,x,x+e,x+e],[h(x),y,y,h(x)],c='r',alpha=0.5)

def plot_mileage_price(cars):
    prices = [c.price for c in cars]
    mileages = [c.mileage for c in cars]
    plt.scatter(mileages, prices, alpha=0.5)
    plt.xlabel('Price ($)', fontsize=16)
    plt.ylabel('Odometer (mi)', fontsize=16)
# Trying out some functions to model our car data:
def p1(x):
    return 25000 - 0.2 * x
def p2(x):
    return 25000 - 0.1 * x
def p3(x):
    return 22500 - 0.1 * x
def p4(x):
    return 20000 - 0.1 * x

# Test data for examples:
test_data = [(-1.0, -2.0137862606487387),
     (-0.9, -1.7730222478628337),
     (-0.8, -1.5510125944820812),
     (-0.7, -1.6071832453434687),
     (-0.6, -0.7530149734137868),
     (-0.5, -1.4185018340443283),
     (-0.4, -0.6055579756271128),
     (-0.3, -1.0067254915961406),
     (-0.2, -0.4382360549665138),
     (-0.1, -0.17621952751051906),
     (0.0, -0.12218090884626329),
     (0.1, 0.07428573423209717),
     (0.2, 0.4268795998864943),
     (0.3, 0.7254661223608084),
     (0.4, 0.04798697977420063),
     (0.5, 1.1578103735448106),
     (0.6, 1.5684111061340824),
     (0.7, 1.157745051031345),
     (0.8, 2.1744401978240675),
     (0.9, 1.6380001974121732),
     (1.0, 2.538951262545233)]

"""
FITTING FUNCTIONS TO DATA

We can use regression to take messy data and modeling it with a simple mathematical function. We can find a function
that approximates a trend in our data. For example, a function p(x) can take mileage as input x and return a 
typical price for a car with that given mileage. We can hypothesise this to be a linear function, p(x) = ax + b,
but the resulting straight diagonal line doesn't come close to most of the data. We use linear regression to find the 
values of a and b so that p(x) follows the trend of the data, i.e. making p(x) the line of best fit.
"""

# Measuring the quality of fit for a function: 

# Calculate the sum of the errors between a function and a data set (the lower the result, the closer the function
# is to representing the data set):
def sum_error(f,data):
    # Take the absolute value of the difference between f(x) and y at each (x,y) point
    errors = [abs(f(x) - y) for (x,y) in data]
    # Sum the results
    return sum(errors)

# Define some functions to test our sum_error() function
def f(x):
    return 2*x
def g(x):
    return 1-x

# Summing the squares of errors: the squared distance function is smooth, so we can use derivatives to minimise it
def sum_squared_error(f,data):
    squared_errors = [(f(x) - y)**2 for (x,y) in data]
    return sum(squared_errors)



# Calculating cost for car price functions

# If we assume cars depreciate in value at a rate of 20 cents per mile, we can describe the price p of a car in terms
# of its mileage x by subtracting 0.2x dollars of depreciation from the starting price ($25,000). This means p(x) is 
# a linear function because it has the form p(x) = -0.2x + 25000.

# We need to measure how well a given linear function predicts the price of a car from its mileage. We can write
# a cost function to do this. It takes a function p(x) as input and returns a number telling us how far it is from the 
# raw data. We can then measure how well the function p(x) = ax + b fits the data set, with any given numbers for a 
# and b, using the cost function.

# Next we write a linear_regression function which automatically finds the best values of a and b, using the gradient
# descent to minimise the values of a and b.

# Takes coefficients a and b and returns the cost of the function p(x) = ax + b:
def coefficient_cost(a,b):
    def p(x):
        return a * x + b
    return sum_squared_error(p, prius_mileage_price)

# Another version of the cost function whose inputs and outputs all have absolute values between 0 and 1:
def scaled_cost_function(c,d):
    return coefficient_cost(0.5*c,50000*d)/1e13

# Find the exponential function of best fit having the form p(x) = qerx, and minimising the sum of the 
# squared error relative to the car data. In this function, e = 2.71828. We will find the values of q 
# and r that have the best fit.

# Takes the coefficients q and r and returns the cost of the corresponding function:
def exp_coefficient_cost(q,r):
    def f(x):
        return q*exp(r*x)  # exp() computes the exponential function e**x
    return sum_squared_error(f,prius_mileage_price)

# Asserting price at 0 miles is $25,000, we can improve our exponential function to fit the data by fixing
# q = 25000:
def exp_cost2(r):
    def f(x):
        return 25000 * exp(r*x)
    return sum_squared_error(f, prius_mileage_price)

# Scaling q (30000) and r (1e-4) values from our linear model:
def scaled_exp_coefficient_cost(s,t):
    return exp_coefficient_cost(30000*s,1e-4*t)/1e11


# EXAMPLES:

# Scatter plot of the test_data data set next to the line f(x) = 2x (fig 14.5):
# plt.scatter([t[0] for t in test_data],[t[1] for t in test_data])
# plot_function(lambda x: 2*x,-1,1,c='k')
# Draw the error values, the differences between the actual y values (in the test_data) and the values predicted by
# the function f(x) = 2x (fig 14.6):
# draw_cost(lambda x: 2*x, test_data)

# Testing our sum_error() function:
# sum_error(f,test_data)  # >> 5.021727176394801
# sum_error(g,test_data)  # >> 38.47711311130152

# Plot the sum of the squared error between a function and a data set (fig 14.9):
# draw_square_cost(lambda x: 2*x, test_data)

# p(x) = -0.2x + 25000 plotted over a scatter plot of the test_data (fig 14.11):
# plot_mileage_price(priuses)
# plot_function(p1,0,125000,c='k')
# Try p2(x) (fig 14.12):
# plot_function(p2,0,250000,c='k')
# Try p3(x) (fig 14.13):
# plot_function(p3,0,225000,c='k')

# Comparing the quality of fit to the data using sum_squared_error:

# sum_squared_error(p1, prius_mileage_price)     # >> 88782506640.24002
# sum_squared_error(p2,prius_mileage_price)      # >> 34723507681.560005
# sum_squared_error(p3, prius_mileage_price)     # >> 22997230681.56001
# sum_squared_error(p4,prius_mileage_price)      # >> 18958453681.560005  > lowest result, best fit

# Demonstrate that sum_error and sum_error_squares both return zero for y = 3x-2
# def line(x):
#     return 3*x-2
# points = [(x, line(x)) for x in range(0,10)]
# sum_error(line,points)  # >> 0
# sum_squared_error(line, points)  # >> 0

# Testing the function f(x) = ax against the test_data data set:
def test_data_coefficient_cost(a):
    def f(x):
        return a* x
    return sum_squared_error(f,test_data)

# Plot the costs for varies values of the slope a (fig 14.14) and the lines represented by each (fig 14.15):
some_slopes = [-1,0,1,2,3]

# Fig 14.14:
#plt.scatter(some_slopes,[test_data_coefficient_cost(a) for a in some_slopes])
#plt.ylabel('cost', fontsize=16)
#plt.xlabel('a', fontsize=16)

# Fig 14.15:
# plt.scatter([t[0] for t in test_data], [t[1] for t in test_data])
# for a in some_slopes:
#     plot_function(lambda x: a*x, -1, 1, c='k')
# plt.ylabel('y', fontsize=16)
# plt.xlabel('x', fontsize=16)

# Plot the test_data_coefficient_cost function (fig 14.16):
# plot_function(test_data_coefficient_cost, -5, 5)
# plt.ylabel('cost', fontsize=16)
# plt.xlabel('a', fontsize=16)

# Cost for the linear function as a heatmap over values of a and b (fig 14.18):
# scalar_field_heatmap(coefficient_cost,-.05,0.5,-50000,50000)
# plt.ylabel('b', fontsize=16)
# plt.xlabel('a', fontsize=16)

# Finding and plotting the line of best fit (fig 14.19):
# c,d = gradient_descent(scaled_cost_function,0,0)
# a = 0.5*c
# b = 50000*d
# def p(x):
#     return a * x + b
# plot_function(p,0,250000,c='k')

# Find the exponential function of best fit having the form p(x) = qerx

# An exponential decay function would fit our car mileage/price data (fig 14.20):
# plot_mileage_price(priuses)
# plt.ylim(-5000,35000)  # Price
# plt.xlim(0,375000)     # Miles
# plot_function(lambda x:0, -50000, 400000, c='gray')
# q,r = (16133.220556990309, -5.951793936498174e-06)
# plot_function(lambda x: q*exp(r*x),0,375000,c='k')

# A heatmap of our scaled exponent coefficients cost function (fig 14.21):
# Shows the lowest cost occurs at a small value of r (t) and a value of q (s) ~0.5
# scalar_field_heatmap(scaled_exp_coefficient_cost,0,1,-1,0)

# Asserting price at 0 miles is $25,000, we can improve our exponential function to fit the data by fixing
# q = 25000. Plotting this function shows that ~r=10**-5 minimises the cost function (fig 14.22):
# plot_function(exp_cost2, -1e-4, 0)

# This implies the best fit function is p(x) = 25000 * (e**(-1.12*(10**-5))) * x   (fig 14.23):
plot_mileage_price(priuses)
plot_function(lambda x: 25000 * exp(-1.12e-5 * x), 0, 350000, c='k')