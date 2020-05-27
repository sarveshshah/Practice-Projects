# PROGRAMS WITH TWO SEPARATE CLASS

from math import atan,sin,cos
import matplotlib.pyplot as plt

class complex:
    """Convert real numbers to complex numbers"""
    def __init__(self, real = 0.0, imaginary = 0.0):
        self.real = real
        self.imaginary = imaginary

    def conjugate(self):
        """Returns the conjugate of the number"""
        return complex(self.real,self.imaginary*-1)

    def add(self,target):
        """Add my complex number to another complex number"""
        return complex(self.real + target.real,self.imaginary + target.imaginary)

    def sub(self,target):
        """Subtract my complex number from another complex number"""
        return complex(self.real - target.real,self.imaginary - target.imaginary)

    def multiply(self,target):
        """Multiply my complex number to another complex number"""
        return complex(self.real*target.real - self.imaginary*target.imaginary,self.real*target.imaginary + target.real*self.imaginary)

    def divide(self,target):
        """Divide my complex number by another complex number"""
        denominator = target.multiply(target.conjugate())
        numerator = self.multiply(target.conjugate())
        return complex(numerator.real/denominator.real,numerator.imaginary/denominator.real)
    
    def polar_form(self):
        """Show polar form of my complex number"""
        return complex_polar((self.real**2+self.imaginary**2)**0.5, atan(self.imaginary/self.real))


    def __repr__(self):
        if self.imaginary<0:
            return ("{:0.2f} - {:0.2f}i".format(self.real,self.imaginary*-1))
        elif self.imaginary>0:
            return ("{:0.2f} + {:0.2f}i".format(self.real,self.imaginary))
        else:
            return "{:0.2f}".format(self.real)
        
class complex_polar:
    """Complex number in polar format"""
    def __init__(self, r = 0.0, theta = 0.0):
        self.r = r
        self.theta = theta

    def ipower(self,n):
        """Returns the nth power of 'i; """
        if n%4 == 0:
            return "1"
        if n%4 == 1:
            return "i"
        if n%4 == 2:
            return "-1"
        if n%4 == 3:
            return "-i"

    def rectangular_form(self):
        """Returns the rectangular form of complex number.\n Accepts theta in radians"""
        return complex(self.r*cos(self.theta),self.r*sin(self.theta))

    def plotpolar(self):
        """Plots polar coordinates using Matplotlib"""
        plt.polar(self.theta,self.r)
    plt.show()

    def __repr__(self):
        if self.theta < 0:
            return '{:0.2f} (cos({:0.2f}) - i sin({:0.2f}))'.format(self.r,self.theta*-1,self.theta*-1)
        else:
            return '{:0.2f} (cos({:0.2f}) + i sin({:0.2f}))'.format(self.r,self.theta,self.theta)

# c1 = complex(5,-2)
# c2 = complex(3,-4)
# r = 5.39
# theta = 0.38

# print(c1.polar_form())
# print(complex.rectangular_form(r,theta))
# print(c1.divide(c2))

c1 = complex(5,-2)
c2 = complex_polar(5.39,0.38)

print(c1)
print(c2)
print(c1.polar_form())