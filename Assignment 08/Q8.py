# 8. Reverse a number
def reverse_no(num):
    rev = 0
    while num > 0:
        rev = rev * 10 + num % 10 
        num //= 10        
    return rev

n = int(input("Enter number: "))
print("Reverse:", reverse_no(n))

