#Q5. Compound Interest 
P = int(input("Enter Principal: "))
R = int(input("Enter Rate: "))
T = int(input("Enter Time: "))

CI = P * ((1 + R/100) ** T) - P
print("Compound Interest =", CI)