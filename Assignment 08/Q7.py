# 7. Sum of n digits
def sum_digits(num):
    total = 0
    while num > 0:
        digit = num % 10      
        total += digit      
        num //= 10            
    return total            

n = int(input("Enter number: "))
print("Sum of digits:", sum_digits(n))