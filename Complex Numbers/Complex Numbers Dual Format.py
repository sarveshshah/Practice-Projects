# PROGRAM THAT CAN MANAGE DUAL FORMAT OF COMPLEX NUMBERS

from math import atan,sin,cos
import matplotlib.pyplot as plt

class complex:
    """Convert real numbers to complex numbers. Accepts rectangular and polar coordinates. Use one of the two at a time"""

    def __init__(self, arg1 = 0.0, arg2 = 0.0, use_polar = False):

        self.use_polar = use_polar

        if use_polar:
            self.r = arg1
            self.theta = arg2
            
        else:
            self.real = arg1
            self.imaginary = arg2

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
        if not self.use_polar:
            return complex(r=(self.real**2+self.imaginary**2)**0.5, theta=atan(self.imaginary/self.real))
        else:
            return "The complex number is already in polar form."


    def rectangular_form(self):
        """Returns the rectangular form of complex number.\n Accepts theta in radians"""
        if self.use_polar:
            return complex(real = self.r*cos(self.theta),imaginary = self.r*sin(self.theta))
        else:
            return "The complex number is in already in rectangular form."


    def plotpolar(self):
        """Plots polar coordinates using Matplotlib"""
        if self.use_polar:
            plt.polar(self.theta,self.r)
            plt.show()
        else:
            print("Cannot plot polar form. The number is in rectangular form")

    # def __repr__(self):
    #     return "Complex number\
    #             \nRectangular form: real = {} i = {}\
    #             \nPolar form: r = {} theta = {}".format(self.real,self.imaginary, self.r, self.theta)

    def show_polar(self):
        if self.use_polar:
            if self.theta < 0:
                return '{:0.2f} (cos({:0.2f}) - i sin({:0.2f}))'.format(self.r,self.theta*-1,self.theta*-1)
            else:
                return '{:0.2f} (cos({:0.2f}) + i sin({:0.2f}))'.format(self.r,self.theta,self.theta)
        else:
            return "The complex number is in rectangular form. Try calling show_rectangular()"
    
    def show_rectangular(self):
        if not self.use_polar:
            if self.imaginary<0:
                return ("{:0.2f} - {:0.2f}i".format(self.real,self.imaginary*-1))
            elif self.imaginary>0:
                return ("{:0.2f} + {:0.2f}i".format(self.real,self.imaginary))
            else:
                return "{:0.2f}".format(self.real)
        else:
            return "The complex number is in polar form. Try calling show_polar()"
                   
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

c1 = complex(5,2)
c2 = complex(5.39,0.38, use_polar=True)


print(c1.show_rectangular())
print(c2.show_polar())

c2.add(c1)