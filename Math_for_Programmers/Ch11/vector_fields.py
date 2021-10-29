from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

# Simplified gravitational vector field function:
def f(x, y):
    return (-x, -y)

# Takes a vector field as a function taking 2D vectors as inputs and returning 2D vectors as 
# outputs and draws a picture of it by drawing the output vectors at a large number of input 
# points in 2D:
def plot_vector_field(f, xmin, xmax, ymin, ymax, xstep=1, ystep=1):
    X, Y = np.meshgrid(np.arange(xmin, xmax, xstep), np.arange(ymin, ymax, ystep))
    U = np.vectorize(lambda x, y: f(x, y)[0])(X, Y)
    V = np.vectorize(lambda x, y: f(x, y)[1])(X, Y)
    plt.quiver(X, Y, U, V, color='red')
    fig = plt.gcf()
    fig.set_size_inches(7,7)

# Draw a plot of f(x,y) as vectors emanating from (x,y) points:
# plot_vector_field(f, -5, 5, -5, 5)

# Another example:
def g(x,y):
    return (-2-x,4-y)

# plot_vector_field(g,-5,5,-5,5)


# Vector fields often arise as results of the calculus operation called the gradient.
# We can write potential energy as a function taking a point (x,y) and returning a number
# representing the gravitational potential energy at the point (x,y).

# We can think of a scalar field as a function that takes (x,y) points as inputs and outputs
# scalars

# This function [u(x,y) = (1/2)*(x**2 + y**2)] defines a scalar field:
# This provides the potential energy for the vector field f(x,y) - (-x, -y)
def u(x,y):
    return 0.5 * (x**2 + y**2)

# Plotting a scalar field as a mesh grid graph:
def plot_scalar_field(f, xmin, xmax, ymin, ymax, xstep=0.25, ystep=0.25, c=None, cmap = cm.coolwarm, alpha = 1, antialiased = False):
    fig = plt.figure()
    fig.set_size_inches(7,7)
    ax = fig.gca(projection='3d')
    fv = np.vectorize(f)
    # Make data
    X = np.arange(xmin, xmax, xstep)
    Y = np.arange(ymin, ymax, ystep)
    X, Y = np.meshgrid(X, Y)
    Z = fv(X, Y)
    # Plot the surface
    surf = ax.plot_surface(X, Y, Z, cmap=cmap, color=c, alpha=alpha, linewidth=0, antialiased=antialiased)

# plot_scalar_field(u, -5, 5, -5, 5)  # >> fig 11.19


# Plotting a scalar field as a heatmap:
def scalar_field_heatmap(f, xmin, xmax, ymin, ymax, xstep=0.1, ystep=0.1):
    fig = plt.figure()
    fig.set_size_inches(7,7)
    fv = np.vectorize(f)
    X = np.arange(xmin, xmax, xstep)
    Y = np.arange(ymin, ymax, ystep)
    X, Y = np.meshgrid(X, Y)
    z = fv(X,Y)
    fig, ax = plt.subplots()
    c = ax.pcolormesh(X, Y, z, cmap='plasma')
    ax.axis([X.min(), X.max(), Y.min(), Y.max()])
    fig.colorbar(c, ax=ax)
    plt.xlabel('x')
    plt.ylabel('y')

# scalar_field_heatmap(u,-5,5,-5,5)  # >> fig 11.20


# Plotting a scalar field as a contour map:
def scalar_field_contour(f, xmin, xmax, ymin, ymax, levels=None):
    fv = np.vectorize(f)
    X = np.arange(xmin, xmax, 0.1)
    Y = np.arange(ymin, ymax, 0.1)
    X, Y = np.meshgrid(X, Y)
    Z = fv(X,Y)
    fig, ax = plt.subplots()
    CS = ax.contour(X,Y,Z,levels=levels)
    ax.clabel(CS, inline=1, fontsize=10, fmt='%1.1f')
    plt.xlabel('x')
    plt.ylabel('y')
    fig.set_size_inches(7,7)

# scalar_field_contour(u,-10,10,-10,10,levels=[10,20,30,40,50,60])  # >> fig 11.21


# A GRADIENT is an operation that takes a scalar field (like potential energy) and 
# produces a vector field (like a gravitational field).
