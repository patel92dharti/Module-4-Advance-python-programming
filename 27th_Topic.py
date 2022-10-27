#What is used to check whether an object o is an instance of class A?

#isinstance(obj, A)
class A:
  name = "John"

y = A()

x = isinstance(y, A)
print(x)