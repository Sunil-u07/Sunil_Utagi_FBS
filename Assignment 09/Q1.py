#Q1. Sum of series using recursive functions: 
def sum_series(n):
    if n == 0:
        return 0
    else:
        return n + sum_series(n - 1)

n = int(input("Enter a number: "))
print("Sum of series:", sum_series(n))
