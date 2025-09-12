#prime or not using recursion
def prime(num, divisor=2): 
    if num < 2:
        return False
    if divisor * divisor > num:
        return True
    if num % divisor == 0:
        return False
    return prime(num, divisor + 1)

n = int(input("Enter number: "))

if prime(n):
    print(f"{n} is a prime number") 
else:
    print(f"{n} is not a prime number")
