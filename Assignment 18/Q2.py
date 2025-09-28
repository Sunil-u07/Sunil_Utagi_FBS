#Q2. Create a class Distance with data members as km,m and cm and add following methods :
#a.  Constructor
#b.  Destructor
#c.  Overload +,- operator


class Distance:
    #a. Constructor
    def __init__(self, km=0, m=0, cm=0):
        self.km = km
        self.m = m
        self.cm = cm
        print("Constructor called")

    #b. Destructor
    def __del__(self):
        print("Destructor called, object deleted")

    #c. Overload + operator
    def __add__(self, other):
        return Distance(self.km + other.km, self.m + other.m, self.cm + other.cm)

    #c. Overload - operator
    def __sub__(self, other):
        return Distance(self.km - other.km, self.m - other.m, self.cm - other.cm)

    def display(self):
        print(f"{self.km} km, {self.m} m, {self.cm} cm")


d1 = Distance(2, 500, 75)
d2 = Distance(1, 200, 50)

d3 = d1 + d2
print("Addition =", end=" ")
d3.display()

d4 = d1 - d2
print("Subtraction =", end=" ")
d4.display()
