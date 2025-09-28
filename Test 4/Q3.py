#Q3. WAP to print "Z" pattern.

def print_Z():
    n = 10 

    # Top row
    print("*" * n)

    # Diagonal 
    for i in range(n-2, 0, -1):
        print(" " * (i-1) + "*")

    # Bottom row
    print("*" * n)

print_Z()
