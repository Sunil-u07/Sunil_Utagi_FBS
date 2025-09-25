#Q6. check if a number is prime or not
n = int(input("Enter a number: "))

if n < 2:
    print("Not Prime")
else:
    for i in range(2, n):
        if n % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
 


# 👉 A prime number is a number greater than 1 that has no divisors other than 1 and itself.
# Examples: prime numbers: 2, 3, 5, 7, 11, 13...
# Non-primes (composite): 4 (2×2), 6 (2×3), 9 (3×3) 