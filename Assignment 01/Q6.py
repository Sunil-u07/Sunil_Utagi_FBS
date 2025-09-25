#Q6. Write a Program to input two angles from user and find third angle of the triangle

A = int(input("Enter first angle: "))
B = int(input("Enter second angle: "))
C = 180 - (A + B)
print("Third angle =", C)