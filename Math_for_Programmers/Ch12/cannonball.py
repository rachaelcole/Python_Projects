import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import numpy as np
from math import sin, cos, pi, sqrt
from random import uniform
from vectors import length

# Helper functions to plot graphs:

# Modelling terrain:
def flat_ground(x,y):
    return 0

def ridge(x,y):
    return (x**2 - 5*y**2) / 2500

# For plotting functions:
def plot_function(f, xmin, xmax, **kwargs):
    ts = np.linspace(xmin, xmax, 1000)
    plt.plot(ts, [f(t) for t in ts], **kwargs)

# Helper functions draw_arrow() and plot_vector_field() to support the graphic overlaying of a vector field on a 
# heatmap:
def draw_arrow(tip, tail, color='k'):
    tip_length = (plt.xlim()[1] - plt.xlim()[0]) / 20.
    length = sqrt((tip[1]-tail[1])**2 + (tip[0]-tail[0])**2)
    new_length = length - tip_length
    new_y = (tip[1] - tail[1]) * (new_length / length)
    new_x = (tip[0] - tail[0]) * (new_length / length)
    plt.gca().arrow(tail[0], tail[1], new_x, new_y, head_width=tip_length/1.5, head_leangth=tip_length/2,fc=color,ec=color)

def plot_vector_field(f, xmin, xmax, ymin, ymax, xsteps=10, ysteps=10, color='k'):
    X,Y = np.meshgrid(np.linspace(xmin,xmax,xsteps),np.linspace(ymin,ymax,ysteps))
    U = np.vectorize(lambda x,y: f(x,y)[0])(X,Y)
    V = np.vectorize(lambda x,y: f(x,y)[1])(X,Y)
    plt.quiver(X,Y,U,V,color=color)
    fig = plt.gcf()

# Takes outputs for results of trajectory() and plots them:
def plot_trajectories(*trajs, show_seconds=False):
    for traj in trajs:
        xs, zs = traj[1], traj[2]
        plt.plot(xs, zs)
        if show_seconds:
            second_indices = []
            second = 0
            for i, t in enumerate(traj[0]):
                if t >= second:
                    second_indices.append(i)
                    second += 1
            plt.scatter([xs[i] for i in second_indices], [zs[i] for i in second_indices])
    xl = plt.xlim()
    plt.plot(plt.xlim(), [0,0], c='k')
    plt.xlim(*xl)

    width = 7
    coords_height = (plt.ylim()[1] - plt.ylim()[0])
    coords_width = (plt.xlim()[1] - plt.xlim()[0])
    plt.gcf().set_size_inches(width, width * coords_height / coords_width)


# Plots 3D trajectories:
def plot_trajectories_3d(*trajs, elevation=flat_ground, bounds=None, zbounds=None, shadows=False):
    fig, ax = plt.gcf(), plt.gca(projection='3d')
    fig.set_size_inches(7,7)
    
    if not bounds:
        xmin = min([x for traj in trajs for x in traj[1]])
        xmax = max([x for traj in trajs for x in traj[1]])
        ymin = min([x for traj in trajs for x in traj[2]])
        ymax = max([x for traj in trajs for x in traj[2]])

        padding_x = 0.1 * (xmax-xmin)
        padding_y = 0.1 * (ymax-ymin)
        xmin -= padding_x
        xmax += padding_x
        ymin -=padding_y
        ymax += padding_y
    else:
        xmin, xmax, ymin, ymax = bounds
    
    plt.plot([xmin,xmax],[0,0],[0,0],c='k')
    plt.plot([0,0],[ymin,ymax],[0,0],c='k')

    g = np.vectorize(elevation)
    ground_x = np.linspace(xmin, xmax, 20)
    ground_y = np.linspace(ymin, ymax, 20)
    ground_x, ground_y = np.meshgrid(ground_x, ground_y)
    ground_z = g(ground_x, ground_y)
    ax.plot_surface(ground_x, ground_y, ground_z, cmap=cm.coolwarm, alpha=0.5, linewidth=0, antialiased=True)

    for traj in trajs:
        ax.plot(traj[1],traj[2],traj[3])
        if shadows:
            ax.plot([traj[1][0],traj[1][-1]],[traj[2][0],traj[2][-1]],[0,0],c='gray',linestyle='dashed')
    
    if zbounds:
        ax.set_zlim(*zbounds)


# Takes outputs of a trajectory() metric and plots the result:
def plot_trajectory_metric(metric, thetas, **settings):
    plt.scatter(thetas, [metric(trajectory(theta, **settings)) for theta in thetas])





# BUILDING A SIMULATION WITH EULER'S METHOD

# We can use the following variable names:
    # x     for horizontal direction
    # z     for vertical directions
    # theta for the angle the cannonball is launched in degrees °
    # v     for the velocity of the cannonball


# Compute the flight path of the cannonball: takes a launch angle (and other params) and returns the positions of the
# cannonball over time until it collides with the earth. Uses Euler's method to simulate motion.
def trajectory(theta, speed=20, height=0, dt=0.01, g=-9.81):
    # Calculate initial x and z components of velocity
    vx = speed * cos(pi * theta / 180)  
    vz = speed * sin(pi * theta / 180)
    t, x, z = 0, 0, height
    # Initialise lists holding all the values of t, x, z over the course of the simulation
    ts, xs, zs = [t], [x], [z]  
    # Run the simulation only while the cannonball is above the ground
    while z >= 0: 
        # Update time, velocity, and position 
        t += dt  
        vz += g * dt
        x += vx * dt
        z += vz * dt
        ts.append(t)
        xs.append(x)
        zs.append(z)
    # Return the lists of t, x, and z values, giving the motion of the cannonball
    return ts, xs, zs  


# Add a y-dimension to compute trajectories in 3D:
def trajectory3d(theta, phi, speed=20, height=0, dt=0.01, g=-9.81, elevation=flat_ground, drag=0):
    vx = speed * cos(pi*theta/180) * cos(pi*phi/180)
    vy = speed * cos(pi*theta/180) * sin(pi*phi/180)
    vz = speed * sin(pi*theta/180)
    t,x,y,z = 0,0,0,height
    ts, xs, ys, zs = [t], [x], [y], [z]
    while z >= elevation(x,y):
        t += dt
        vx -= (drag * vx) * dt
        vy -= (drag * vy) * dt
        vz += (g - (drag * vz)) * dt
        x += vx * dt
        y += vy *dt
        z += vz * dt
        ts.append(t)
        xs.append(x)
        ys.append(y)
        zs.append(z)
    return ts, xs, ys, zs

# Takes a launch angle and returns the range of the cannonball at that angle
def landing_position(traj):
    return traj[1][-1]

# Compute the time the cannonball spends in the air
def hang_time(traj):
    return traj[0][-1]

# Compute the maximum height of the cannonball
def max_height(traj):
    return max(traj[2])




# SOLVING FOR THE RANGE OF THE PROJECTILE IN 3D


# Set up constants
B = 0.0004
C = 0.005
v = 20
g = -9.81

def velocity_components(v, theta, phi):
    vx = v * cos(theta*pi/180) * cos(phi*pi/180)
    vy = v * cos(theta*pi/180) * sin(phi*pi/180)
    vz = v * sin(theta*pi/180)
    return vx, vy, vz

# This encodes the function r(𝜃, 𝜙):
def landing_distance(theta, phi):
    vx, vy, vz = velocity_components(v, theta, phi)
    v_xy = sqrt(vx**2 + vy**2)
    a = (g/2) - B * vx**2 + C * vy**2
    b = vz
    landing_time = -b/a
    landing_distance = v_xy * landing_time
    return landing_distance




# CALCULATING THE OPTIMAL RANGE


# Range as a function of angle r(𝜃): Tells us the range of the cannon at every launch angle
def r(theta):
    return (-2*20*20/-9.81)*sin(theta * pi/180)*cos(theta*pi/180)


# The function r(theta, phi) [r(𝜃, 𝜙)] tells us the range of the cannon at these launch angles. 
# We can plot r(𝜃, 𝜙) using a heatmap:
def scalar_field_heatmap(f, xmin, xmax, ymin, ymax, xsteps=100, ysteps=100):
    fig = plt.figure()
    fig.set_size_inches(7,7)
    fv = np.vectorize(f)
    # Make data
    X = np.linspace(xmin, xmax, xsteps)
    Y = np.linspace(ymin, ymax, ysteps)
    X, Y = np.meshgrid(X, Y)
    z = fv(X,Y)
    fig,ax = plt.subplots()
    # Plot surface
    c = ax.pcolormesh(X,Y,z,cmap='plasma')
    ax.axis([X.min(), X.max(), Y.min(), Y.max()])
    fig.colorbar(c, ax=ax)

# We can also plot r(𝜃, 𝜙)(as a scalar field) as a surface graph:
def plot_scalar_field(f, xmin, xmax, ymin, ymax, xsteps=100, ysteps=100, c=None, cmap=cm.coolwarm, alpha=1, antialiased=False):
    fig = plt.gcf()
    fig.set_size_inches(7,7)
    ax = fig.gca(projection='3d')
    fv = np.vectorize(f)
    # Make data
    X = np.linspace(xmin, xmax, xsteps)
    Y = np.linspace(ymin, ymax, ysteps)
    X, Y = np.meshgrid(X,Y)
    Z = fv(X,Y)
    # Plot the surface
    surf = ax.plot_surface(X,Y,Z,cmap=cmap,color=c,alpha=alpha,linewidth=0,antialiased=antialiased)



# GRADIENTS

# Finding the uphill direction with the gradient: first step is to take the slopes of small secant lines
# Find the slope of a secant line f(x) between x values of xmin and xmax:
def secant_slope(f, xmin, xmax):
    return (f(xmax) - f(xmin)) / (xmax - xmin)

# The approximate derivative is a secant line bwteen x - 10-6 and x + 10-6
def approx_derivative(f, x, dx=1e-6):
    return secant_slope(f, x-dx, x+dx)

# The partial derivative of ∂f/∂x at (x0,y0) is the ordinary derivative of f(x,y0) with respect to x at x = x0 
# The partial derivative of ∂f/∂y at (x0,y0) is the ordinary derivative of f(x0,y) with respect to y at y = y0
# The gradient is a vector (tuple) of these partial derivatives:
def approx_gradient(f, x0, y0, dx=1e-6):
    partial_x = approx_derivative(lambda x: f(x, y0), x0, dx=dx)
    partial_y = approx_derivative(lambda y: f(x0, y), y0, dx=dx)
    return (partial_x, partial_y)

# We can store the special function, approx_gradient, representing the landing_distance() function's gradient:
def landing_distance_gradient(theta, phi):
    return approx_gradient(landing_distance, theta, phi)


# Takes as input a function to optimise and a pair of starting inputs, and uses the gradient ▽r(𝜃, 𝜙) of the 
# function r(𝜃, 𝜙) to find the optimal value(s). We know f’(x) = 0 when f attains its maximum value.
def gradient_ascent(f, xstart, ystart, tolerance=1e-6):
    # Set initial values of (x,y) to the input values
    x = xstart
    y = ystart
    # Tells us how to move uphill from the current (x,y) value
    grad = approx_gradient(f,x,y)
    # Only step to a new point if the gradient is longer than the minimum length
    while length(grad) > tolerance:
        # Update (x,y) to ▽f(x,y)
        x += grad[0]
        y += grad[1]
        # Update the gradient at this new point
        grad = approx_gradient(f, x, y)
    # When nowhere further uphill to go, return the values of (x,y)
    return x, y

# Gradient points
def gradient_ascent_points(f, xstart, ystart, tolerance=1e-6):
    x = xstart
    y = ystart
    xs, ys = [x], [y]
    grad = approx_gradient(f,x,y)
    while length(grad) > tolerance:
        x += grad[0]
        y += grad[1]
        grad = approx_gradient(f,x,y)
        xs.append(x)
        ys.append(y)
    return xs, ys

# Count gradient ascent steps
def count_ascent_points(f,x,y,rate=1):
    gap = gradient_ascent_points(f,x,y,rate=rate)
    print(gap[0][-1],gap[1][-1])
    return len(gap[0])



# EXAMPLES:

# Plotting two trajectories to compare them:
traj1 = trajectory(45)
traj2 = trajectory(60)
# plot_trajectories(traj1, traj2)  # fig 12.6

# Plotting every angle from 0-95° in increments of 5:
angles = range(0,90,5)
landing_positions = [landing_position(trajectory(theta)) for theta in angles]
# plt.scatter(angles, landing_positions)  # fig 12.3

# Plotting trajectories with seconds shown (fig 12.9):
# plot_trajectories(trajectory(20), trajectory(45), trajectory(60), trajectory(80), show_seconds=True)

# Scatter plot of hang time vs angle for angles from 0-180:
test_angles = range(0,181,5)
hang_times = [hang_time(trajectory(theta)) for theta in test_angles]
# plt.scatter(test_angles, hang_times)  # fig 12.8

# Using the metrics:
# plot_trajectory_metric(hang_time, range(0,181,5))  # fig 12.8.2
# plot_trajectory_metric(landing_position, range(0,90,5), height=10)  # fig 12.5

# Show a graph of z(t) with theta = 45 degrees:
trj = trajectory(45)
ts, zs = trj[0], trj[2]
# plt.plot(ts,zs)  # fig 12.11

# Plot projectile range as a function of the launch angle (up to 90°):
# fig 12.17
# plot_function(r,0,90)

# Solving for the maximum range:
# r(45)   # >> 40.774719673802245
# r(135)  # >> -40.77471967380224

# Plotting a 3D trajectory:
# plot_trajectories_3d(trajectory3d(45,45))     # fig 12.18
# plot_trajectories_3d(trajectory3d(20,-20,elevation=ridge),     # Fig 12.19
# trajectory3d(20,-20,elevation=ridge, drag=0.1), bounds=[0,40,-40,0], elevation=ridge)  

# Plot a heatmap of the range of the cannon as a function of the launch angles theta (x-axis) and phi (y-axis):
# The brightest spots occur when the range of the projectile is maximised
# scalar_field_heatmap(landing_distance,0,90,0,360)      # (fig 12.21)

# If we make a 3D plot of r(𝜃, 𝜙), we can see that it is flat at its maximum points (fig 12.23):
# plot_scalar_field(landing_distance,0,90,0,360)

# Plot of the gradient vector field ▽r(𝜃, 𝜙) on top of the heatmap of the function r(𝜃, 𝜙). The arrows point in the 
# direction of increase in r (range), towards brighter spots on the heatmap (fig 12.25):
# scalar_field_heatmap(landing_distance,0,90,0,360)
# plot_vector_field(landing_distance_gradient,0,90,0,360,xsteps=10,ysteps=10,color='k')
# plt.xlabel('theta')
# plt.ylabel('phi')
# plt.gcf().set_size_inches(9,7)


# The same plots as above, but zoomed in to near (𝜃, 𝜙) = (37.5°, 90°), the approx location of one of the 
# maxima (fig 12.26):
# scalar_field_heatmap(landing_distance,35,40,80,100)
# plot_vector_field(landing_distance_gradient,35,40,80,100,xsteps=10,ysteps=15,color='k')
# plt.xlabel('theta')
# plt.ylabel('phi')
# plt.gcf().set_size_inches(9,7)

# Plot the start and end points for the gradient  ascent from an initial point of (𝜃, 𝜙) = (36°, 83°) to a new 
# location of ~ (𝜃, 𝜙) = (37.58°, 90.00°) (fig 12.28):
# scalar_field_heatmap(landing_distance, 35, 40, 80, 100)
# plt.scatter([36,37.58114751557887],[83,89.99992616039857],c='k',s=75)
# plt.plot(*gradient_ascent_points(landing_distance,36,83),c='k')
# plt.xlabel('theta')
# plt.ylabel('phi')
# plt.gcf().set_size_inches(9,7)

# Plot the paths of gradient ascent from 20 random points (fig 12.29):
# scalar_field_heatmap(landing_distance,0,90,0,360)
# plt.xlabel('theta')
# plt.ylabel('phi')
# gap = gradient_ascent_points(landing_distance,60,190,1000)

# for x in range(0,20):
#     gap = gradient_ascent_points(landing_distance,uniform(0,90),uniform(0,360))
#     plt.plot(*gap,c='k')
# plt.gcf().set_size_inches(9,7)


# Start the gradient ascent at 180° to find where on r(𝜃, 𝜙) the gradient is 0:
# gradient_ascent(landing_distance,0,180)  # returns (46.122613357930206, 180.0)
