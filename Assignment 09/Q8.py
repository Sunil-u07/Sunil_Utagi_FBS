#Q8. prime or not using recursion
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
 


# 👉 A prime number is a number greater than 1 that has no divisors other than 1 and itself.
# Examples: prime numbers: 2, 3, 5, 7, 11, 13...
# Non-primes (composite): 4 (2×2), 6 (2×3), 9 (3×3)