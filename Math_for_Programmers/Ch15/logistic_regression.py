"""
CLASSIFICATION PROBLEMS

A classification problem is one where you have one or more pieces of raw data and you want to say what kind of object 
each piece of data represents.

We can build machine learning algorithms for classification where the more real data the algorithm sees, the more it 
learns, and the better it performs at the classification task.

Using our car_data, we can write an algorithm that gives a yes (1) or no (0) answer as to whether a car is a BMW or a 
Prius, for example. Our classification model takes in a vector and produces a number between 0 and 1, representing the 
confidence that the vector represents a BMW instead of a Prius.


LOGISTIC REGRESSION

We can build our classifier using logistic regression. A logistic function takes a pair of input numbers and produces
a single output number that is always between 0 and 1. Our classification function is the logistic function that best
fits the sample data we provide.

Logistic functions take 3 parameters, so we need to write a cost function for the logistic function that finds the 3
parameters that minimise the cost function using gradient descent.
"""
import matplotlib.pyplot as plt
import numpy as np
from math import exp, log
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from vectors import length
# import car data
from car_data import bmws, priuses

# Helper functions:
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

def plot_scalar_field(f,xmin,xmax,ymin,ymax,xsteps=100,ysteps=100,c=None,cmap=cm.coolwarm,alpha=1,antialiased=False,zorder=0):
    fig = plt.gcf()
    fig.set_size_inches(7,7)
    ax = fig.gca(projection='3d')
    fv = np.vectorize(f)
    # Make data
    X = np.linspace(xmin,xmax,xsteps)
    Y = np.linspace(ymin,ymax,ysteps)
    X,Y = np.meshgrid(X,Y)
    Z = fv(X,Y)
    # Plot surface
    surf = ax.plot_surface(X,Y,Z,cmap=cmap,color=c,alpha=alpha,linewidth=0,antialiased=antialiased,zorder=zorder)

def plot_line(acoeff,bcoeff,ccoeff,**kwargs):
    a,b,c = acoeff,bcoeff,ccoeff
    # black by default
    if 'c' not in kwargs:
        kwargs['c'] = 'k'
    if b == 0:
        plt.plot([c/a,c/a],[0,1])
    else:
        def y(x):
            return (c-a*x)/b
        plt.plot([0,1],[y(0),y(1)],**kwargs)

# Testing a classification function on real data

# Load the data:
all_car_data = []
for bmw in bmws:
    all_car_data.append((bmw.mileage,bmw.price,1))
for prius in priuses:
    all_car_data.append((prius.mileage,prius.price,0))

# CLASSIFICATION FUNCTIONS

# Let's use some simple logic to decide if a car is a BMW - if the price is > $25,000, it's a BMW (59% accurate):
def bmw_finder(mileage,price):
    if price > 25000:
        return 1
    else:
        return 0

# Updating our classifier function to lower the price threshold to $20,000 for a BMW (73.5% accurate):
def bmw_finder2(mileage,price):
    if price > 20000:
        return 1
    else:
        return 0

# Updated classifier function from eyeballing the graphs, called a decision boundary (80.5% accurate):
def decision_boundary_classify(mileage, price):
    if price > 21000 - 0.07 * mileage:
        return 1
    else:
        return 0

# Builds a classifier function for any specified, constant cut-off price. Returns true if price > cutoff, otherwise false:
def constant_price_classifier(cutoff_price):
    def c(x,p):
        if p > cutoff_price:
            return 1
        else:
            return 0
    return c

# Test the accuracy of a cut-off value:
def cutoff_accuracy(cutoff_price):
    c = constant_price_classifier(cutoff_price)
    return test_classifier(c, all_car_data)


# TESTING OUR CLASSIFICATION FUNCTIONS

# Measure the performance of our algorithm: takes a classification function and a dataset as input and returns a %
# value of how many cars the classification function identifies correctly:
def test_classifier(classifier, data, verbose=False):
    true_positives = 0
    false_positives = 0
    true_negatives = 0
    false_negatives = 0
    for mileage, price, is_bmw in data:
        predicted = classifier(mileage,price)
        if predicted and is_bmw:
            true_positives += 1
        elif predicted:
            false_positives += 1
        elif is_bmw:
            false_negatives += 1
        else:
            true_negatives += 1
    result = (true_positives + true_negatives) / len(data)
    if verbose:
        print(f'Percent correct: {result * 100}%')
        print(f'True positives: {true_positives}')
        print(f'True negatives: {true_negatives}')
        print(f'False positives: {false_positives}')
        print(f'False negatives: {false_negatives}')
    return result

# Another way to test our success at classification is by thinking of our data as 2D vectors and plotting them on a 2D plane:
def plot_data(ds):
    plt.scatter([d[0] for d in ds if d[2]==0],[d[1] for d in ds if d[2]==0],c='C1')
    plt.scatter([d[0] for d in ds if d[2]==1],[d[1] for d in ds if d[2]==1],c='C0',marker='x')
    plt.ylabel('Price ($)', fontsize=16)
    plt.xlabel('Odometer (mi)', fontsize=16)


# CLASSIFICATION AS A REGRESSION PROBLEM

# First we should rescale our data:
def make_scale(data):
    # The max and min provide the current range for the data set
    min_val = min(data)
    max_val = max(data)
    # Put the data poiint at the same fraction of the way between 0 and 1 as it was from min_val to max_val
    def scale(x):
        return (x-min_val) / (max_val - min_val)
    # Reverse it 
    def unscale(y):
        return y * (max_val - min_val) + min_val
    return scale, unscale

# The most basic logistic function is called a sigmoid function σ(x):
# This function sends any input number to a value between 0 and 1. Big negative nums are closer to 0, and big positive
# nums are closer to 1. The result of σ(0) is 0.5
def sigmoid(x):
    return 1 / (1+exp(-x))

# We can write our decision boundary function from earlier as f(x,p) = p - ax - b, where x is mileage and p is price
# On the decision boundary, f(x,p) returns 0. We want a version of f(x,p) that returns 0.5 on the decision boundary,
# 1 for a BMW, and 0 for a Prius. We can do this using a sigmoid σ function. If we pass the result of f into a sigmoid σ
# function, we get a new function, L(x,p) = σ(f(x,p)). We want the L(x,p) that best fits our dataset.

# Takes 3 params and returns the logistic function they define:
def make_logistic(a,b,c):
    def l(x,p):
        return sigmoid(a*x + b*p - c)
    return l

# A simple way to measure the cost of the function L is to find how far off it is from the correct value (0 or 1), and 
# add all these error values to get a total value telling you how far the L(x,p) function comes from the dataset:
def simple_logistic_cost(a,b,c):
    l = make_logistic(a,b,c)
    errors = [abs(is_bmw-l(x,p)) for x,p,is_bmw in scaled_car_data]
    return sum(errors)

# To find the cost of a given point, calculate how close the given logstic function comes to the wrong answer, and take the
# negative logarithm of the result:
def point_cost(l,x,p,is_bmw):
    wrong = 1 - is_bmw
    return -log(abs(wrong - l(x,p)))

# Takes the params that define a logistic function and returns a number measuring how far the logistic function is from the
# dataset: the lower the value returned, the better the predictions from the associated logic function
def logistic_cost(a,b,c):
    l = make_logistic(a,b,c)
    errors = [point_cost(l,x,p,is_bmw) for x,p,is_bmw in scaled_car_data]
    return sum(errors)


# FINDING THE BEST LOGISTIC FUNCTION

# Calculations for our gradient taken from chs 12 and 14:
def secant_slope(f, xmin, xmax):
    return (f(xmax) - f(xmin)) / (xmax - xmin)

def approx_derivative(f, x, dx=1e-6):
    return secant_slope(f, x-dx, x+dx)

def partial_derivative(f,i,v,**kwargs):
    def cross_section(x):
        arg = [(vj if j != i else x) for j,vj in enumerate(v)]
        return f(*arg)
    return approx_derivative(cross_section, v[i], **kwargs)

# A function that can calculate the gradient of a function in any number of dimensions:
def approx_gradient(f,v,dx=1e-6):
    return [partial_derivative(f,i,v) for i in range(0,len(v))]

# We need to get the 3D gradient using the 3 partial derivatives of a function f(x,y,z) as components of a 3D vector:
def approx_gradient3(f,x0,y0,z0,dx=1e-6):
    partial_x = approx_derivative(lambda x:f(x,y0,z0),x0,dx=dx)
    partial_y = approx_derivative(lambda y:f(x0,y,z0),y0,dx=dx)
    partial_z = approx_derivative(lambda z:f(x0,y0,z),z0,dx=dx)
    return (partial_x, partial_y, partial_z)

# A gradient descent function that can take in a function in any number of dimensions:
def gradient_descent(f,vstart,tolerance=1e-6,max_steps=1000):
    v = vstart
    grad = approx_gradient(f,v)
    steps = 0
    while length(grad) > tolerance and steps < max_steps:
        v = [(vi - 0.01 * dvi) for vi,dvi in zip(v,grad)]
        grad = approx_gradient(f,v)
        steps += 1
    return v

# 3D gradient descent:
def gradient_descent3(f,xstart,ystart,zstart,tolerance=1e-6,max_steps=1000):
    x = xstart
    y = ystart
    z = zstart
    grad = approx_gradient3(f,x,y,z)
    steps = 0
    while length(grad) > tolerance and steps < max_steps:
        x -= 0.01 * grad[0]
        y -= 0.01 * grad[1]
        z -= 0.01 * grad[2]
        grad = approx_gradient3(f,x,y,z)
        steps += 1
    return x,y,z

# Using the values calculated from our gradient descent 3D function, we can write a logistic classifier function that
# takes in a mileage (x) and price (p) of a car and returns a number between 0 and 1 measuring how likely it is to be a 
# BMW (1) instead of a Prius (0):
def best_logistic_classifier(x,p):
    l = make_logistic(3.716700362680151, 11.42206250284465, 5.596878415978096)
    if l(x,p) > 0.5:
        return 1
    else: 
        return 0

# Return the sum of the squared differences of a function from 1:
def sum_squares(*v):
    return sum([(x-1)**2 for x in v])


# EXAMPLES

# Testing our human-logic bmw_finder() function:
# test_classifier(bmw_finder,all_car_data,verbose=True)  # >> Returns 0.59, i.e., 59% accuracy

# Testing our bmw_finder2() function:
# test_classifier(bmw_finder2,all_car_data,verbose=True)  # >> Returns 0.735, or, 73.5% accurate

# Next, we can plot the dataset to understand what's qualitatively wrong with our bmw_finder() functions, to help see where
# we can improve the classification with our logistic classification function (fig 15.2):
# plot_data(all_car_data)  # BMWs are blue 'x's; Priuses are orange circles

# By plotting the lines of our bmw_finder funcs, we can see which is a better fit visually (bmw_finder2):
# plot_function(lambda x: 25000, 0, 200000, c='k')  # Plotting our bmw_finder() line (black)
# plot_function(lambda x: 20000,0,200000)  # Our bmw_finder2() line (blue)  (fig 15.3)

# To get a better fit, we can plot a line that slopes downward at approx the same rate as the 15.2 graph using
# the equation p(x) = 21000 - 0.07x, where p is price and x is mileage (fig 15.4):
# plot_function(lambda x: 21000 - 0.07 * x, 0, 200000, c='k')

# We can test this equation using our test_classifier() function:
# test_classifier(decision_boundary_classify, all_car_data, verbose=True)  # >> 80.5% accurate

# Check each price and find if it is the best cutoff price using the max() function, so we can maximise the cutoff_accuracy
# function:
# all_prices = [price for (mileage, price, is_bmw) in all_car_data]
# max(all_prices, key=cutoff_accuracy)  # >> 17998.0
# Using the above, we know $17998 is the best price to use as a cutoff when deciding if a car is a BMW or a Prius
# Testing our cutoff price:
# test_classifier(constant_price_classifier(17998.0), all_car_data, verbose=True)  # >> 79.5% accurate

# Scale our data:
price_scale, price_unscale = make_scale([x[1] for x in all_car_data])
mileage_scale, mileage_unscale = make_scale([x[0] for x in all_car_data])
scaled_car_data = [(mileage_scale(mileage), price_scale(price), is_bmw) for mileage,price,is_bmw in all_car_data]
# plot_data(scaled_car_data)  # (fig 15.7)


# From eyeballing the scaled dataset, we find the function p(x) = 0.56 - 0.35x gives price at the decision boundary as a 
# function of mileage (fig 15.8):
# plot_function(lambda x: 0.56 - 0.35*x,0,1,c='k')

# A heatmap shows a similar positive result (fig 15.9):
# scalar_field_heatmap(lambda x,p: p + 0.35*x - 0.56, 0, 1, 0, 1)
# plt.ylabel('Price', fontsize=16)
# plt.xlabel('Mileage', fontsize=16)
# plot_function(lambda x: 0.56 - 0.35*x,0,1,c='k')

# Graph of a sigmoid function σ(x) (fig 15.10):
# plot_function(sigmoid,-5,5)

# Testing different logistic functions: p = 0.56 - 0.35x and x + p = 1 (fig 15.18)
# plot_data(scaled_car_data)
# plot_line(0.35,1,0.56)
# plot_line(1,1,1,c='C0')

# Confirming the first logistic function is a better fit than the second:
# logistic_cost(0.35,1,0.56)   # >> 130.92490748700456 > lower cost, better fit
# logistic_cost(1,1,1)         # >> 135.56446830870456 > higher cost, worse fit

# Drawing the graph of k(x,y) = σ(x**2 + y**2 - 1) (fig 15.19):
def k(x,y):
    return sigmoid(x**2 + y**2 - 1)
# plot_scalar_field(k, -3, 3, -3, 3)

# Drawing the logistic functions σ(2x+y-1) (fig 15.20) and σ(4x+2y-2) (fig 15.21)
# plot_scalar_field(lambda x,y: sigmoid(2*x+y-1),-3,3,-3,3)  # fig 15.20
# plot_scalar_field(lambda x,y: sigmoid(4*x+2*y-2),-3,3,-3,3)  # fig 15.21

# Using gradient descent to find the best fit
# gradient_descent3(logistic_cost,1,1,1,max_steps=100)  # >> (0.2111449358903251, 5.045439728633814, 2.1260122572155717)
# gradient_descent3(logistic_cost,1,1,1,max_steps=200)  # >> (0.8845715268219687, 6.657543187631611, 2.9550572858514967)
# gradient_descent3(logistic_cost,1,1,1,max_steps=8000)  # >> (3.716700362680151, 11.42206250284465, 5.596878415978096)

# Comparing our eyeballed best guess estimate (black) with the gradient descent algorithm result (blue) (fig 15.22):
# plot_data(scaled_car_data)
# plot_line(0.35,1,0.56)  # p(x) = 0.35x + p - 0.56
# plot_line(3.716700362680151, 11.42206250284465, 5.596878415978096,c='C0')  # p(x) = 3.716x + 11.422p - 5.597

# If we compare the previous best guess sigmoid logistic function with our gradient descent algorithm sigmoid logistic
# function (the optimised logistic function), we can see the optimised logistic function is much steeper, meaning its
# certainty that a car is a BMW rather than a Prius increases rapidly as you cross the decision boundary:

# σ(0.35x + p - 0.56) (fig 15.23)
# plot_scalar_field(make_logistic(0.35,1,0.56),-2,2,-2,2) 
# σ(3.716x + 11.422p - 5.597) (fig 15.24):
# plot_scalar_field(make_logistic(3.7167003153580045,11.422062409195114,5.596878367305919), -2, 2, -2, 2) 

# 5 dimensions:
# v = [2,2,2,2,2]
# gradient_descent(sum_squares,v)  # >> [1.0000002235452137, 1.0000002235452137, 1.0000002235452137, 1.0000002235452137, 1.0000002235452137]