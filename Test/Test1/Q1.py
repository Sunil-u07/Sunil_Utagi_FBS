import math

L = float(input("Enter length: "))
B = float(input("Enter breadth: "))
R = float(input("Enter radius: "))

# Area calculation
area_rectangle = L * B
area_semi_circle = 0.5 * math.pi * R * R
total_area = area_rectangle + area_semi_circle

# Perimeter calculation
perimeter = (2 * L) + (2 * R) + (math.pi * R)

print("Area =", total_area)
print("Perimeter =", perimeter)