from abc import ABCMeta, abstractmethod, abstractproperty  # Abstract base class
from vectors import *
from PIL import Image
from matrices import *
from datetime import datetime, timedelta

# Vector base class
# Defines an abstract base class, a class not intended to be instantiated, but designed as a template for classes to inherit from
class Vector(metaclass=ABCMeta):  
    # All child classes will inherit the methods in this class
    # The @abstractmethod decorator means a method is not implemented in the base class and needs to be implemented for any child class
    @abstractmethod
    def scale(self, scalar):
        pass
    @ abstractmethod
    def add(self, other):
        pass
    @classmethod  # Zero is a class method because there's only one zero value for any vector space
    @abstractproperty  # also an abstract property because it isn't defined yet
    def zero():
        pass
    # Operator overloading:
    def __add__(self, v2):
        # Override the + operator to mean vector addition
        return self.add(v2)
    # Override the * operator to mean scalar multiplication
    def __mul__(self, scalar):
        return self.scale(scalar)
    def __rmul__(self, scalar):
        return self.scale(scalar)
    def subtract(self, other):
        return self.add(-1 * other)
    def __sub__(self, other):
        return self.subtract(other)
    # Override negation:
    def __neg__(self):
        return self.scale(-1)
    # Divide vectors by scalars:
    def __truediv__(self, scalar):
        return self.scale(1.0/scalar)


# Class inheriting from Vector with an abstract property representing the dimension
class CoordinateVector(Vector):
    @abstractproperty
    def dimension(self):
        pass
    def __init__(self, *coordinates):
        self.coordinates = tuple(x for x in coordinates)
    def add(self, other):
        return self.__class__(*add(self.coordinates, other.coordinates))
    def scale(self, scalar):
        return self.__class__(*scale(scalar, self.coordinates))
    def __repr__(self):
        return (f'{self.__class__.__qualname__}{self.coordinates}')


# Class representing zero-dimensional vectors; set of vectors with zero coordinates that we can 
# describe as empty tuples:
class Vec0(Vector):
    def __init___(self):
        pass
    def add(self, other):
        return Vec0()
    def scale(self, scalar):
        return Vec0()
    @classmethod
    def zero(cls):
        return Vec0()
    def __eq__(self, other):
        return self.__class__ == other.__class__ == Vec0
    def __repr__(self):
        return "Vec0()"


# Class representing vectors with one coordinate:
class Vec1(Vector):
    def __init__(self, x):
        self.x = x
    def add(self, other):
        return Vec1(self.x + other.x)
    def scale(self, scalar):
        return Vec1(scalar * self.x)
    @classmethod
    def zero(cls):
        return Vec1(0)
    def __eq__(self, other):
        return self.x == other.x
    def __repr__(self):
        return (f'Vec1({self.x})')


# Class representing 2D coordinate vectors:
class Vec2(Vector):  # Inherits methods from Vector abstract base class
    # We can initialise a vector with 'v = Vec2(1.6, 3.8)' and access its coordinates with v.x and v.y  
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def add(self, other):
        # add() takes a second vector as an argument and returns a new Vec2 object whose coordinates are
        # the sum of the x and y coordinates:
        assert self.__class__ == other.__class__
        return Vec2(self.x + other.x, self.y + other.y)
    def scale(self, scalar):
        # Takes a scalar as input and returns a new, scaled Vec2 instance as output
        return Vec2(scalar * self.x, scalar * self.y)
    # Implement the zero method:
    @classmethod
    def zero(cls):
        return Vec2(0, 0)
    def __eq__(self, other):
        # Override the equality method for Vec2 objects
        assert self.__class__ == other.__class__
        return self.x == other.x and self.y == other.y
    # Change the string representation of Vec2 objects:
    def __repr__(self):
        return(f'Vec2({self.x}, {self.y})')


# Class representing 3D vectors:
class Vec3(Vector):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def add(self, other):
        assert self.__class__ == other.__class__
        return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)
    @classmethod
    def zero(cls):
        return Vec3(0, 0, 0)
    def scale(self, scalar):
        return Vec3(scalar * self.x, scalar * self.y, scalar * self.z)
    def __eq__(self, other):
        assert self.__class__ == other.__class__
        return (self.x == other.x and self.y == other.y and self.z == other.z)
    def __repr__(self):
        return(f'Vec3({self.x}, {self.y}, {self.z})')

# A 6D vector class:
class Vec6(CoordinateVector):
    def dimension(self):
        return 6
    @classmethod
    def zero(cls):
        return Vec6(0,0,0,0,0,0)

# Class representing a function as a vector
class Function(Vector):
    def __init__(self, f):
        self.function = f
    def add(self, other):
        return Function(lambda x: self.function(x) + other.function(x))
    def scale(self, scalar):
        return Function(lambda x: scalar * self.function(x))
    @classmethod
    def zero(cls):
        return Function(lambda x: 0)
    # Lets us treat this as a function:
    def __call__(self, arg):
        return self.function(arg)

# Stores a function of 2 variables ike f(x, y) = x + y
class Function2(Vector):
    def ___init__(self, f):
        self.function = f
    def add(self, other):
        return Function(lambda x,y: self.function(x,y) + other.function(x,y))
    def scale(self, scalar):
        return Function(lambda x,y: scalar * self.function(x,y))
    @classmethod
    def zero(cls):
        return Function(lambda x,y: 0)
    def __call__(self, *args):
        return self.function(*args)

# Class representing a linear function (like 'f(x) = ax + b') as a vector:
class LinearFunction(Vec2):
    def __call__(self, input):
        return self.x * input + self.y

# Class representing a quadratic function (ax**2 + bx + c) as a vector:
class QuadraticFunction(Vector):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def add(self, v):
        return QuadraticFunction(self.a + v.a, self.b + v.b, self.c + v.c)
    def scale(self, scalar):
        return QuadraticFunction(scalar * self.a, scalar * self.b, scalar * self.c)
    def __call__(self, x):
        return self.a * x * x + self.b * x + self.c
    @classmethod
    def zero(cls):
        return QuadraticFunction(0,0,0)

# Class representing a polynomial as a vector:
class Polynomial(Vector):
    def __init__(self, *coefficients):
        self.coefficients = coefficients
    def __call__(self, x):
        return sum(coefficient * x ** power for (power, coefficient) in enumerate(self.coefficients))
    def add(self, p):
        return Polynomial([a+b for a,b in zip(self.coefficients, p.coefficients)])
    def scale(self, scalar):
        return Polynomial([scalar * a for a in self.coefficients])
    def _repr_latex_(self):
        monomials = [repr(coefficient) if power == 0
        else "x ^ {%d}" % power if coefficient == 1
        else "%s x ^ {%d}" % (coefficient, power)
        for (power, coefficient) in enumerate(self.coefficients)
        if coefficient != 0]
        return "$ %s $" % (" + ".join(monomials))
    @classmethod
    def zero(cls):
        return Polynomial(0)


# Matrix lass inheriting from Vector 
class Matrix(Vector):
    @abstractproperty
    def rows(self):
        pass
    @abstractproperty
    def columns(self):
        pass
    def __init__(self, entries):
        self.entries = entries
    def add(self, other):
        return self.__class__(tuple(tuple(self.entries[i][j] + other.entries[i][j] 
        for j in range(0,self.columns())) for i in range(0,self.rows())))
    def scale(self, scalar):
        return self.__class__(tuple(tuple(scalar * e for e in row) 
        for row in self.entries))
    def __repr__(self):
        return (f'{self.__class__.__qualname__}{self.entries}')
    def zero(self):
        return self.__class__(
            tuple(
                tuple(0 for i in range(0,self.columns())) 
                for j in range(0, self.rows())))


# A class representing 5x3 matrices thought of as vectors
class Matrix5_by_3(Matrix):
    def rows(self):
        return 5
    def columns(self):
        return 3
# 2x2 matrix:
class Matrix2_by_2(Matrix):
    def rows(self):
        return 2
    def columns(self):
        return 2


# We can think of each instance of CarForSale as a vector
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


"""
# 2D vector math:
v = Vec2(3,4)  # Creates a new Vec2 object called v with x-coord of 3 and y-coord of 4
w = v.add(Vec2(-2,6))  # Adds a second Vec2 to v to produce a new Vec2 instance called w
print(w.x)  # Prints the x-coordinate of w

vec2_object_instance = 3.0 * Vec2(1,0) + 4.0 * Vec2(0,1)
print(vec2_object_instance)

print(Vec2(1,3) - Vec2(5,1))


# 3D vector math:
vec3 = 2.0 * (Vec3(1,0,0) + Vec3(0,1,0))
print(vec3)

# 6D vector math!
print(Vec6(1,2,3,4,5,6) + Vec6(1,2,3,4,5,6))
"""
