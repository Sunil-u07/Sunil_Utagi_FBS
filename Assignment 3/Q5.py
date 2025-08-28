# 5. Check whether the triangle is equilateral, isosceles or scalene triangle.
a=int(input("Enter side a: "))
b=int(input("Enter side b: "))
c=int(input("Enter side c: "))

if (a == b == c):
    print("The triangle is equilateral.")
elif (a == b or b == c or a == c):
    print("The triangle is isosceles.")
else:
    print("The triangle is scalene.")
