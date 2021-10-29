"""
RATES OF CHANGE

Calculus includes concepts called the derivative and the integral.

The derivative takes a function and gives you another function representing its rate of change.

The integral takes a function representing a rate of change and gives you the original function measuring the
cumulative value.

The following example will measure volume/rate of change of oil in a pump/barrels per litre (bbl).
"""

import matplotlib.pyplot as plt
import numpy as np



# HELPER FUNCTIONS

# Helper functions to plot our graphs:
def plot_function(f, tmin, tmax, tlabel=None, xlabel=None, axes=False, **kwargs):
    ts = np.linspace(tmin,tmax,1000)
    if tlabel:
        plt.xlabel(tlabel, fontsize=18)
    if xlabel:
        plt.ylabel(xlabel, fontsize=18)
    plt.plot(ts, [f(t) for t in ts], **kwargs)
    if axes:
        total_t = tmax - tmin
        plt.plot([tmin-total_t/10, tmax+total_t/10],[0,0],c='k',linewidth=1)
        plt.xlim(tmin-total_t/10,tmax+total_t/10)
        xmin, xmax = plt.ylim()
        plt.plot([0,0],[xmin,xmax],c='k',linewidth=1)
        plt.ylim(xmin, xmax)

def plot_volume(f, tmin, tmax, axes=False, **kwargs):
    plot_function(f,tmin,tmax, tlabel="time (hr)", xlabel="volume (bbl)", axes=axes, **kwargs)

def plot_flow_rate(f, tmin, tmax, axes=False, **kwargs):
    plot_function(f,tmin,tmax, tlabel="time(hr)", xlabel="flow rate (bbl/hr)", axes=axes, **kwargs)



# VOLUME

# Takes t in hours as an argument and returns the volume of oil in the tank at that time in bbl
def volume(t):
    return (t-4)**3 / 64 +3.3

# Plot flow rate over time with linear volume
def linear_volume_function(t):
    return 5*t + 3

# For decreasing volumes:
def decreasing_volume(t):
    if t < 5:
        return 10 - (t**2)/5
    else:
        return 0.2*(10-t)**2



# FLOW RATES

# Gives flow rate in bbl/hr over time
def flow_rate(t):
    return 3*(t-4)**2 / 64

# Get the average flow rate given volume and time at 2 points
def average_flow_rate(v,t1,t2):
    return (v(t2) - v(t1)) / (t2 - t1)

# Get the average flow rate of different intervals on a graph:
def interval_flow_rates(v,t1,t2,dt):
    # v = the volume function
    # t1 = start time
    # t2 = end time
    # dt = the fixed duration of time intervals
    return [(t,average_flow_rate(v,t,t+dt)) for t in np.arange(t1,t2,dt)]



# PLOTTING

# Get the secant line of a function
def secant_line(f,x1,x2):
    def line(x):
        return f(x1) + (x-x1) * (f(x2) - f(x1)) / (x2 - x1)
    return line

# Plot the secant line of a function between 2 given points
def plot_secant(f,x1,x2,color='k'):
    line = secant_line(f,x1,x2)
    plot_function(line,x1,x2,c=color)
    plt.scatter([x1,x2],[f(x1), f(x2)], c=color)

# Plot interval flow rates:
def plot_interval_flow_rates(volume,t1,t2,dt):
    series = interval_flow_rates(volume,t1,t2,dt)
    times = [t for (t,_) in series]
    rates = [q for (_,q) in series]
    plt.scatter(times, rates)



# DERIVATIVES
# We can use the derivative to get the instantaneous flow rate at a given time
# For example, the slope of the tangent line to the volume graph at t = 1 gives us the best 
# measure of the instantaneous flow rate at t = 1. N.b. tangent lines only work with smooth
# functions. The slope of the tangent is called the derivative of the function at the point.

# Takes a volume function (v) and a single point in time (t) and returns an approximation
# of the instantaneous flow rate at that time, given in bbl/hour
def instantaneous_flow_rate(v, t, digits=6):
    # If two numbers differ by less than a tolerance of 10**-d, then they agree to d decimal places:
    tolerance = 10 ** (-digits)
    h = 1
    # Calculate a first secant line slope on an interval spanning h=1 units on either side of the target point t
    approx = average_flow_rate(v, t-h, t+h)
    # Try 2-digit iterations before giving up on convergence:
    for i in range(0, 2*digits):
        h = h / 10
        # Calculate the slope of a new secant line around the point t on a 10x smaller interval
        next_approx = average_flow_rate(v, t-h, t+h)
        if abs(next_approx - approx) < tolerance:
            # If the two approxes differ by less than the tolerance, round the result and return it:
            return round(next_approx, digits)
        else:
            # Run the loop again with a smaller interval
            approx = next_approx
    # If we exceed the max iterations, the procedure has not converged to a result
    raise Exception('Derivative did not converge')

# Curried version of instantaneous_flow_rate(): takes a volume function (v) and returns
# a function that takes a time and returns an instantaneous flow rate function
def get_flow_rate_function(v):
    def flow_rate_function(t):
        instantaneous_flow_rate(v, t)
    return flow_rate_function




# INTEGRALS
# We start with a known flow rate function and recover the volume function in a process called integration.

# Take a flow rate function (q), a time (t), and a duration (dt), and return the approx. change in volume from 
# time (t) to time (t) + duration (dt):
def small_volume_change(q,t,dt):
    return q(t) * dt

# Calculate the volume change on any time interval (approximates definite integrals):
def volume_change(q,t1,t2,dt):
    return sum(small_volume_change(q,t,dt) for t in np.arange(t1,t2,dt))

# Takes a flow rate (q), initial volume (v0), a small time interval (dt), and a time (T) in question
# and returns a volume function:
def approximate_volume(q,v0,dt,T):
    return v0 + volume_change(q,0,T,dt)

# Curried version of approximate_volume to give the function giving the approx volume at a given time:
def approximate_volume_function(q,v0,dt):
    def volume_function(T):
        return approximate_volume(q,v0,dt,T)
    return volume_function

# Takes a flow rate function and returns a function giving the cumulative volume over time
# Find the volume at any point to an arbitrary position (gives the integral of the flow rate)
def get_volume_function(q,v0,digits=6):
    def volume_function(T):
        tolerance = 10 ** (-digits)
        dt = 1
        approx = v0 + volume_change(q,0,T,dt)
        for i in range(0,digits*2):
            dt = dt/10
            next_approx = v0 + volume_change(q,0,T,dt)
            if abs(next_approx - approx) < tolerance:
                return round(next_approx,digits)
            else:
                approx = next_approx
        raise Exception('Did not converge!')
    return volume_function




# DEMONSTRATIONS

# Plot the volume (fig 8.3):
# plot_volume(volume,0,10)

# Plot a decreasing volume (fig 8.6):
# plot_volume(decreasing_volume,0,10)

# Plot a volume and its secant line (fig 8.8):
# plot_volume(volume,0,10)
# plot_secant(volume,4,8)


# Get the interval flow rate in each hour (fig 8.9):
# rates = interval_flow_rates(volume,0,10,1)  # Returns a list of the flow rate in each hour

# Plot interval flow rates on a scatter plot for 1-hr intervals (fig 8.10):
# plot_interval_flow_rates(volume,0,10,1)

# Plot interval flow rates on a scatter plot for 20-min intervals (fig 8.11):
# plot_interval_flow_rates(volume,0,10,1/3)
# Add the flow rate:
# plot_flow_rate(flow_rate,0,10)

# Plot the decreasing volume flow rates over time at 0.5-hr intervals (fig 8.12):
# plot_interval_flow_rates(decreasing_volume, 0, 10, 0.5)

# Plot linear volume flow rate over time (constant) (fig 8.13):
# plot_interval_flow_rates(linear_volume_function, 0, 10, 0.25)

# Plotting the flow_rate() function alongside the get_flow_rate() function shows the 
# graphs are identical (fig 8.17):
# plot_function(flow_rate, 0, 10)
# plot_function(get_flow_rate_function(volume), 0, 10)

# Confirm the graph of the volume function is not a straight line on the interval from 0.999hrs to
# 1.0001 hours (by showing the secant line has a different value than the volume() function at t=1)
# volume(1)  >> Returns 2.878125
# secant_line(volume,0.999,1.001)(1) >> Returns 2.8781248593749997


# How much oil is added to the tank in the first 6 hours?
first6 = volume_change(flow_rate,0,6,0.01)
print(f'About {first6:.2f} bbls of oil are added to the tank in the first 6 hours')
# How much in the last 4 hours?
last4 = volume_change(flow_rate,6,10,0.01)
print(f'About {last4:.2f} bbls of oil are added in the last 4 hours')


# Plot the volume_function() against our original volume() for volume(0) - 2.3 
# and at 0.01hr intervals (fig 8.29):
plot_function(approximate_volume_function(flow_rate,2.3,0.01),0,10)
plot_function(volume,0,10)