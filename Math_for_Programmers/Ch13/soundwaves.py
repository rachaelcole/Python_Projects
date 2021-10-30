from math import sin, cos, pi, sqrt, tan
import matplotlib.pyplot as plt
import numpy as np
import pygame, pygame.sndarray


# SOUNDWAVES


# Function to plot functions on a graph:
def plot_function(f, xmin, xmax, **kwargs):
    ts = np.linspace(xmin,xmax,1000)
    plt.plot(ts, [f(t) for t in ts], **kwargs)
    
# Function to plot an array of integer values:
def plot_sequence(points,max=100,line=False,**kwargs):
    if line:
        plt.plot(range(0,max),points[0:max],**kwargs)
    else:
        plt.scatter(range(0,max),points[0:max],**kwargs)

# Produces a sine function either stretched or compressed vertically and horizontally to 
# produce a more pleasant sound
def make_sinusoid(frequency, amplitude):
    def f(t):  # Define the sinusoidal function that will be returne
        return amplitude * sin(2*pi*frequency*t)
    return f

# Gets the number of values of f(t) in the range of t values between start and end
def sample(f,start,end,count):
    mapf = np.vectorize(f)
    ts = np.arange(start,end,(end-start)/count)
    values = mapf(ts)
    return values.astype(np.int16)

# Make a constant f(x) = 1/sqrt(2) function
def const(n):
    return 1/sqrt(2)

# Fourier series function: takes a constant, and lists a and b containing the coefficients
def fourier_series(a0,a,b):
    def result(t):
        # Evaluate all cosine terms with their constants and add the results
        cos_terms = [an*cos(2*pi*(n+1)*t) for (n,an) in enumerate(a)]
        # Do the same for sine terms
        sin_terms = [bn*sin(2*pi*(n+1)*t) for (n,bn) in enumerate(b)]
        # Add both results with the constant coefficient times the value of the constant function (1)
        return a0*const(t) + sum(cos_terms) + sum(sin_terms)
    return result

# DECOMPOSING A SOUND WAVE INTO ITS FOURIER SERIES

# Defining an inner product for periodic functions:
def inner_product(f,g,N=1000):
    dt = 1/N
    return 2*sum([f(t)*g(t)*dt for t in np.arange(0,1,dt)])

# Create the the nth sine function:
def s(n):
    def f(t):
        return sin(2*pi*n*t)
    return f

# Create the nth cosine function:
def c(n):
    def f(t):
        return cos(2*pi*n*t)
    return f

# Takes a function and number of coefficients and returns the Fourier coefficient representing the 
# constant function, and 2 lists of Fourier coefficients:
def fourier_coefficients(f,N):
    a0 = inner_product(f,const)
    an = [inner_product(f,c(n)) for n in range(1,N+1)]
    bn = [inner_product(f,s(n)) for n in range(1,N+1)]
    return a0, an, bn

# Finding the Fourier coefficients of a square/sawtooth/speedbump shaped wave:
def square(t):
    return 1 if (t % 1) < 0.5 else -1

def sawtooth(t):
    return t%1

def modified_sawtooth(t):
    return 8000 * sawtooth(441*t)

def speedbumps(t):
    if abs(t%1 - 0.5) > 0.25:
        return 0
    else:
        return sqrt(0.25*0.25 - (t%1 - 0.5)**2)



# Initialise the sound library
pygame.mixer.init(frequency=44100, size=-16)




# EXAMPLES:
# Generate 1 second of white noise by creating a NumPy array of 44,100 random integers from -32,768-32,767
# arr = np.random.randint(-32768, 32767, size=44100)
# Make the array 2-dimensional to play on 2 channels
# arr = np.repeat(arr.reshape(44100, 1), 2, axis=1)
# Plotting our random array, arr (fig 13.5):
# plot_sequence(arr)
# Plotting our random array with lines to show a theoretical soundwave (fig 13.6):
# plot_sequence(arr,line=True,max=441)
# Play the sound:
# sound = pygame.sndarray.make_sound(arr)
# sound.play()  # Plays 1 second of white noise

# Plot of the sequence consisting of 10,000 numbers repeated 50 times, followed by -10,000 numbers
# peated 50 times (fig 13.7):
# form = np.repeat([10000, -10000], 50)
# plot_sequence(form)
# np.tile() repeats a given array a specified number of times (fig 13.8):
# arr = np.tile(form,441)
# plot_sequence(arr, line=True, max=1000)

# Make the new array 2D:
# arr = np.repeat(arr.reshape(44100, 1), 2, axis=1)
# Play the new sound (the note A):
# sound = pygame.sndarray.make_sound(arr)
# sound.play()

# Plot a sinusoidal function with a frequency of 5Hz and an amplitude of 4, from t=0 to t=1 (fig 13.14):
# plot_function(make_sinusoid(5,4),0,1)

# Make a sinusoid with a frequency of 441Hz and an amplitude of 8000
# sinusoid = make_sinusoid(441,8000)
# Plot 1 second of the sinusoid soundwave (fig 13.15):
# plot_function(sinusoid,0,1)
# arr = sample(sinusoid, 0, 1, 44100)
# arr = np.repeat(arr.reshape(44100, 1), 2, axis=1)
# sound = pygame.sndarray.make_sound(arr)
# sound.play()

# Plot the tangent function tan(t) = sin(t)/cos(t) (fig 13.16):
# plot_function(tan,0,5*pi)
# plt.ylim(-10,10)

# Plot the function cos(kt) from 0-1 with a frequency of 5 (fig 13.17):
# plot_function(lambda t: cos(10*pi*t),0,1)

# Combine two sounds to make a chord:
sample1 = sample(make_sinusoid(441,8000),0,1,44100)
sample1_2d = np.repeat(sample1.reshape(44100, 1), 2, axis=1)
sample2 = sample(make_sinusoid(551,8000),0,1,44100)
sample2_2d = np.repeat(sample2.reshape(44100, 1), 2, axis=1)

# Make and play the two samples
sound1 = pygame.sndarray.make_sound(sample1_2d)
sound2 = pygame.sndarray.make_sound(sample2_2d)
# sound1.play()
# sound2.play()

# Make and play the chord
chord = pygame.sndarray.make_sound(sample1_2d + sample2_2d)
# chord.play()

# Plot the two samples (fig 13.18):
# plot_sequence(sample1,max=400)
# plot_sequence(sample2,max=400)

# Plot the chord (fig 13.19):
# plot_sequence(sample1 + sample2,max=400)

# Fourier series sin(8*pi*t) + sin(10*pi*t) (fig 13.19.1):
f = fourier_series(0,[0,0,0,0,0],[0,0,0,1,1])
# plot_function(f,0,1)

# More fourier series (fig 13.20)
f1 = fourier_series(0,[],[4/pi])
f3 = fourier_series(0,[],[4/pi,0,4/(3*pi)])
# plot_function(f1,0,1)
# plot_function(f3,0,1)

# Using list comprehensions with fourier series (fig 13.21):
b = [4/(n*pi) if n%2 != 0 else 0 for n in range(1,10)]
f4 = fourier_series(0,[],b)
# plot_function(f4,0,1)

#arr = sample(lambda t:1000*f(441*t), 0, 1, 44100)
#arr = np.repeat(arr.reshape(44100, 1), 2, axis=1)
#sound = pygame.sndarray.make_sound(arr)
#sound.play()