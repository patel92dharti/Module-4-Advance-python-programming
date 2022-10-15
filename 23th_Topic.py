"""
Write a Python class named Rectangle constructed by a length and width and
a method which will compute the area of a rectangle
"""
class Rect:
    def rectangle(self,length,width):
        self.length=length
        self.width=width
    def putArea(self):
        return self.length*self.width
Rectangle=Rect()
Lenght=int(input("Enter the Rectangle Length:"))
Width=int(input("Enter the Rectangle Width:"))
Rectangle.rectangle(Lenght,Width)
print("Area of Rectangle is",Rectangle.putArea())
