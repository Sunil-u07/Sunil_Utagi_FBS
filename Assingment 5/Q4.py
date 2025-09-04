n = int(input("Enter a number: "))
order = len(str(n))  
temp = n
sum_pow = 0

while temp > 0:
    digit = temp % 10
    sum_pow += digit ** order
    temp //= 10

if sum_pow == n:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")
