import numpy as np
import matplotlib.pyplot as plt
from math import sin
from PIL import Image
from tests import *
from classes import *
from colors import *
from functions_as_vectors import *
from matrices import *
from matrices_as_vectors import *
from vectors import *


# Class representing an image as a vector:
class ImageVector(Vector):
    # Handle images of a fixed size (300x300px)
    size = (300, 300)  
    
    def __init__(self, input):
        try:
            img = Image.open(input).resize(ImageVector.size)  # Accepts name of an image file
            self.pixels = img.getdata()
        except:
            self.pixels = input  # Also accepts pixel lists directly
    
    def image(self):
        img = Image.new('RGB', ImageVector.size)  # 
        img.putdata([(int(r), int(g), int(b)) for (r,g,b) in self.pixels])
        return img
    
    # Add two image vectors to make a new image by adding the RGB values for each pixel
    def add(self, img2):
        return ImageVector([(r1+r2,g1+g2,b1+b2) 
        for ((r1,g1,b1),(r2,g2,b2)) 
        in zip(self.pixels, img2.pixels)])
    
    # Perform scalar multiplication by multiplying every RGB pixel by the scalar
    def scale(self, scalar):
        return ImageVector([(scalar *r, scalar*g, scalar*b) 
        for (r,g,b) in self.pixels])
    
    @classmethod
    def zero(cls):
        # Zero RGB content in every pixel
        total_pixels = cls.size[0] * cls.size[1]
        return ImageVector([(0,0,0) for _ in range(0, total_pixels)])
    
    def _repr_png_(self):
        # For Jupyter notebooks display
        return self.image()._repr_png_()


# Sample image manipulation
0.5 * ImageVector("inside.jpg") + 0.5 * ImageVector("outside.jpg")

# Subtracting an image from an all-white image will invert its colours:
white = ImageVector([(255,255,255) for _ in range(0,300*300)])  # define our own white image by a pixel grid
white - ImageVector("outside.jpg")


# Returns a solid-colour image vector with the given RGB values at every pixel:
def solid_color(r,g,b):
    return ImageVector([(r,g,b) for _ in range(0,300*300)])


# A linear map that generates an ImageVector from a 30x30 grayscale image, implemented
# as a 30x30 matrix of brightness values:
image_size = (300,300)
total_pixels = image_size[0] * image_size[1]
square_count = 30  # Breaking the img into a 30x30 grid
square_width = 10

def ij(n):
    return (n // image_size[0]. n % image_size[1])

# Take an ImageVector and return an array of 30 arrays with 30 values each, giving
# grayscale values for each square
def to_lowres_grayscale(img):  
    matrix = [[0 for i in range(0,square_count)] for j in range(0,square_count)]
    for (n,p) in enumerate(img.pixels):
        i, j = ij(n)
        weight = 1.0 / (3 * square_width * square_width)
        matrix[i // square_width][j // square_width] += (sum(p) * weight)
    return matrix

# Takes a 30x30 matrix and returns an image built from 10x10pixel blocks with brightness
# given by the matrix values
def from_lowres_grayscale(matrix):
    def lowres(pixels, ij):
        i,j = ij
        return pixels[i // square_width][j // square_width]
    def make_highres(limg):
        pixels = list(matrix)
        triple = lambda x: (x,x,x)
        return ImageVector([triple(lowres(matrix, ij(n))) for n in range(0, total_pixels)])
    return make_highres(matrix)