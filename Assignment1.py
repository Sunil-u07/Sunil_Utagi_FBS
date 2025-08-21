import math

#Q1. Percentage of Student
m1 = int(input("Enter marks of subject 1: "))
m2 = int(input("Enter marks of subject 2: "))
m3 = int(input("Enter marks of subject 3: "))
m4 = int(input("Enter marks of subject 4: "))
m5 = int(input("Enter marks of subject 5: "))

total = m1 + m2 + m3 + m4 + m5
percentage = (total / 500) * 100
print("The percentage of the student is:", percentage, "%")


#Q2. Area of Rectangle
print("\n--- Area of Rectangle ---")
length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))
print("The area of the rectangle is:", length * breadth)

 
#Q3. Quotient and Remainder
print("\n--- Quotient and Remainder ---")
a = int(input("Enter dividend: "))
b = int(input("Enter divisor: "))
print("The quotient is:", a // b, "and the remainder is:", a % b)

#Q4. Simple Interest
P = float(input("Enter Principal: "))
R = float(input("Enter Rate: "))
T = float(input("Enter Time: "))

SI = (P * R * T) / 100
print("Simple Interest =", SI)

#Q5. Compound Interest 
P = float(input("Enter Principal: "))
R = float(input("Enter Rate: "))
T = float(input("Enter Time: "))

CI = P * ((1 + R/100) ** T) - P
print("Compound Interest =", CI)

#Q6. Third angle of triangle
A = float(input("Enter first angle: "))
B = float(input("Enter second angle: "))
C = 180 - (A + B)
print("Third angle =", C)

#Q7. Roots of quadratic equation
import cmath

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# Calculate the discriminant
D = (b**2) - (4*a*c)

# two solutions
sol1 = (-b - cmath.sqrt(D)) / (2*a)
sol2 = (-b + cmath.sqrt(D)) / (2*a)

print(f"The solutions are {sol1} and {sol2}")

#Q8. Convert days
days = int(input("Enter number of days: "))
years = days // 365
weeks = (days % 365) // 7
remaining_days = (days % 365) % 7
print("Years:", years, "Weeks:", weeks, "Days:", remaining_days)

#Q9. Area of triangle
base = float(input("Enter base: "))
height = float(input("Enter height: "))
print("Area of Triangle =", 0.5 * base * height) 

#Q10. Area of equilateral triangle
side = float(input("Enter side: "))
area = (math.sqrt(3) / 4) * side**2
print("Area of Equilateral Triangle =", area)

#Q11. Circle area and circumference
r = float(input("Enter radius: "))
print("Area of Circle =", math.pi * r**2)
print("Circumference of Circle =", 2 * math.pi * r)

#Q12. Volume of sphere
r = float(input("Enter radius: "))
print("Volume of Sphere =", (4/3) * math.pi * r**3)