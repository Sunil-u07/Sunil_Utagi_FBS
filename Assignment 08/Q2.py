#2. Area of Circle
import math

def area_circle(r):
    return math.pi * r ** 2

r = int(input("Enter radius: "))
print("Area of Circle:", area_circle(r))
