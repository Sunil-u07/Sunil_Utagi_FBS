# 11. Armstrong number
def armstrong(num):
    sum_pow = 0
    power = len(str(num))
    temp = num

    while temp > 0:
        digit = temp % 10
        sum_pow += digit ** power
        temp //= 10
        
    return sum_pow == num
 
n = int(input("Enter a number: ")) 

if armstrong(n):
    print(f"{n} is an Armstrong Number")
else:
    print(f"{n} is Not an Armstrong Number")

#153 = 1³ + 5³ + 3³ = 1 + 125 + 27 = 153 
#1634 = 1⁴ + 6⁴ + 3⁴ + 4⁴ = 1 + 1296 + 81 + 256 = 1634   