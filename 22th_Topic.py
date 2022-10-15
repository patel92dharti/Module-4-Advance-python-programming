#How to Define a Class in Python? What Is Self? Give An Example Of A Python Class
"""
Python is an object-oriented programming language.
Almost everything in Python is an object, with its properties and methods.
A Class is like an object constructor, or a "blueprint" for creating objects.
"""
"""
The self parameter is a reference to the current instance of the class, 
and is used to access variables that belongs to the class.
"""
class A:
    def getNumber(self,n):
        self.n=n%2*10
    def putout(self):
        print("Your Amount is",self.n)
d1=A()
d1.getNumber(int(input("Enter the number:")))
d1.putout()