#Q4. Check if a number is an Armstrong number
#compare with assignment 8 , Q11]

n = int(input("Enter a number: "))

sum_pow = 0
power = len(str(n))  
temp = n

while temp > 0:
    digit = temp % 10
    sum_pow += digit ** power
    temp //= 10


if sum_pow == n:
    print(f"{n} is an Armstrong Number")
else:
    print(f"{n} is Not an Armstrong Number")
