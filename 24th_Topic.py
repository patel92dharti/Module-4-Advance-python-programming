"""
Write a Python class named Circle constructed by a radius and two methods
which will compute the area and the perimeter of a circle
"""
from math import pi
class circle:
    def inputN(self,r):
        self.radius=r
    def area(self):
        return self.radius**2*pi
    def perimeter(self):
        return 2*(self.radius*pi)
d1=circle()
d1.inputN(4)
print(d1.area())
print(d1.perimeter())