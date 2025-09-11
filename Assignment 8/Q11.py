# 11. Armstrong number
def armstrong(num):
    sum_pow = 0
    temp = num
    power=0

   # Count number of dgt
    t = num
    while t > 0:
        power += 1
        t //= 10

    # Cal sum of dgts power
    t = num
    while t > 0:
        digit = t % 10
        sum_pow += digit ** power
        t //= 10
    return num == sum_pow

n = int(input("Enter number: "))

if armstrong(n):
    print(f"{n} is an Armstrong Number")
else:
    print(f"{n} is Not an Armstrong Number")
