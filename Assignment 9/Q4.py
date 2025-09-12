#sum of first n natural numbers 
def sum_n(n):
    if n == 0:
        return 0
    return n + sum_n(n - 1)

n = int(input("Enter number: "))
print("Sum of first n natural numbers:", sum_n(n))
