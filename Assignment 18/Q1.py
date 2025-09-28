#Q1. Create a class Complex Number with data members as real and imag and addfollowing methods :
#a.  Constructor
#b.  Destructor
#c.  Overload +,- operator


class ComplexNumber:
     #a. Constructor
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag
        print("Constructor called") 
    
    #b. Destructor
    def __del__(self):
        print("Destructor called, object deleted")

    #c. Overload + operator
    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)
    
    #c. Overload - operator
    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    def display(self):
        print(f"{self.real} + {self.imag}i")


c1 = ComplexNumber(4, 5)
c2 = ComplexNumber(2, 3)

c3 = c1 + c2
print("Addition =", end=" ")
c3.display()

c4 = c1 - c2
print("Subtraction =", end=" ")
c4.display()