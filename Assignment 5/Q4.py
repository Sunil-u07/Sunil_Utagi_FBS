def armstrong(num):
    temp = num
    sum_pow = 0
    order = 0
    
    # count digits
    while temp > 0:
        temp //= 10
        order += 1
    
    temp = num
    # sum of digits
    while temp > 0:
        digit = temp % 10
        sum_pow += digit ** order
        temp //= 10
    
    return sum_pow == n  

n = int(input("Enter a number: "))

if armstrong(n):
    print(f"{n} is an Armstrong Number")
else:
    print(f"{n} is Not an Armstrong Number")
