from draw2d import *
from math import pi, sin, cos
from vectors import add, scale

"""
t = 0
s = (0,0)
v = (1,0)
a = (0,0.2)
dt = 0.1
steps = 100

positions = [s]

# Get 6 values of vector s, corresponding to the times t = 0, 2, 4, 6, 8, 10
for _ in range(0,100):
    t+= 2
    # Update position by adding the change in position to the current position
    s = add(s, scale(dt,v))
    # Update the velocity by adding the change in velocity to the current velocity
    v = add(v, scale(dt, a))
    positions.append(s)
"""
# Fig 9.5: Points on the object's trajectory according to our Euler's method calculation:
# draw2d(Points2D(*positions))

def pairs(lst):
    return list(zip(lst[:-1],lst[1:]))

# A function that carries out Euler's method automatically for a constantly accelerating
# object (n.b., under-approximates the y-axes):
def eulers_method(s0,v0,a,total_time,step_count):
    trajectory = [s0]
    s = s0
    v = v0
    dt = total_time / step_count
    for _ in range(0, step_count):
        s = add(s,scale(dt,v))
        v = add(v,scale(dt,a))
        trajectory.append(s)
    return trajectory


# Over-approximate the y-axes:
def eulers_method_overapprox(s0,v0,a,total_time,step_count):
    trajectory = [s0]
    s = s0
    v = v0
    dt = total_time / step_count
    for _ in range(0, step_count):
        v = add(v,scale(dt,a))
        s = add(s,scale(dt,v))
        trajectory.append(s)
    return trajectory


# Demonstrate the trajectory of a baseball thrown at 30m/s at an angle of 20 degrees up
# from the positive x direction using Euler's method:
angle = 20 * pi/180
s0 = (0,1.5)  # initial position is (0, 1.5)
v0 = (30*cos(angle),30*sin(angle))  # initial velocity
a = (0, -9.81)  # gravity constant is 9.81m/s/s toward the earth

result = eulers_method(s0,v0,a,3,100)


# Euler's method demonstrations:
approx5 = eulers_method((0,0), (1,0), (0,0.2), 10, 5)
approx10 = eulers_method((0,0), (1,0), (0,0.2), 10, 10)
approx100 = eulers_method((0,0), (1,0), (0,0.2), 10, 100)
approx1000 = eulers_method((0,0), (1,0), (0,0.2), 10, 1000)

draw2d(
    Points2D(*approx5, color='C0'),
    *[Segment2D(t,h,color='C0') for (h,t) in pairs(approx5)],
    Points2D(*approx10, color='C1'),
    *[Segment2D(t,h,color='C1') for (h,t) in pairs(approx10)],
    *[Segment2D(t,h,color='C2') for (h,t) in pairs(approx100)],
    *[Segment2D(t,h,color='C3') for (h,t) in pairs(approx1000)]
)