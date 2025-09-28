#Q1. Write a function to which we pass a parameter andprint the factors of a given number.

def print_factors(n):
    print(f"Factors of {n}: ", end="")
    for i in range(1, n+1):
        if n % i == 0:
            print(i, end=" ")
    print()

print_factors(12)
