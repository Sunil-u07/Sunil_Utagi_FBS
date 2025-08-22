#Q5. Compound Interest 
P = float(input("Enter Principal: "))
R = float(input("Enter Rate: "))
T = float(input("Enter Time: "))

CI = P * ((1 + R/100) ** T) - P
print("Compound Interest =", CI)