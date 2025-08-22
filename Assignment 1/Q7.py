#Q7. Roots of quadratic equation
import cmath

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# Calculate the discriminant
D = (b**2) - (4*a*c)

# Calculate the two solutions
sol1 = (-b - cmath.sqrt(D)) / (2*a)
sol2 = (-b + cmath.sqrt(D)) / (2*a)

print(f"The solutions are {sol1} and {sol2}")