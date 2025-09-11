import math

# a) 1 + 2 + 3 + … + n
def sum_series(n):
    return sum(range(1, n+1))
n=int(input("Enter number: "))
print("Sum of series (a):", sum_series(n))

# b) 1! + 2! + 3! + … + n!
def sum_fact(n):
    total = 0
    for i in range(1, n+1):
        total += math.factorial(i)
    return total
n=int(input("Enter number: "))
print("Sum of factorials (b):", sum_fact(n))


# c) 1^1 + 2^2 + 3^3 + … + n^n
def sum_powers(n):
    total = 0
    for i in range(1, n+1):
        total += i**i
    return total
n=int(input("Enter number: "))
print("Sum of powers (c):", sum_powers(n))

