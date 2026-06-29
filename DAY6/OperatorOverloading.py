print(10+20)
print("Hello"+"Guys")
print(5*4)
print("hi"*4)
#Custom Operator Overloading
class Book:
    def __init__(self,pages):
        self.pages=pages

#magic method
    def __add__(self,other):
        return self.pages+others.pages

b1=Book(200)
b2=Book(300)
print(b1+b2)