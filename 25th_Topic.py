#Explain Inheritance in Python with an example? What is init? Or What Is A Constructor In Python?

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