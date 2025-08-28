#Q3.input angles of a triangle and check whether triangle is valid or not.
a = int(input("Enter angle a: "))
b = int(input("Enter angle b: "))
c = int(input("Enter angle c: "))

if (a + b + c == 180 ):
    print("Valid Triangle")
else:
    print("Invalid Triangle")
