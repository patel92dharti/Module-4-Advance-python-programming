#Explain Inheritance in Python with an example? What is init? Or What Is A Constructor In Python?

"""
What is init?
The __init__ function is called every time an object is created from a class.
The __init__ method lets the class initialize the object's attributes and serves no other purpose.
It is only used within classes.
"""
"""
What Is A Constructor In Python?
The constructor is a method that is called when an object is created of a class. 
The creation of the constructor depends on the programmer, or else Python will automatically generate the default constructor. 
It can be used in three types - Parameterized Constructor, Non-Parameterized Constructor, Default Constructor.
"""

class A:
    def getA(self,a):
        self.a=a
    def returenA(self):
        return "A is Char",self.a
class B(A):
    def getB(self,b):
        self.b=b
    def returenB(self):
        return "B is Char",self.b
class C(B):
    def getC(self,c):
        self.c=c
    def returenC(self):
        return "C is Char",self.c

c1=C()
c1.getC(50)
print(c1.returenC())
c1.getB("Dharti")
print(c1.returenB())
c1.getA("Life is Nothing")
print(c1.returenA())