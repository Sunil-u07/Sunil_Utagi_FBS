#Q8. Solve following:
#a. 1! + 2! + 3! + 4! + …..n!
n = int(input("Enter n: "))

total = 0
fact = 1

for i in range(1, n+1):
    fact *= i        # calculate factorial step by step
    total += fact    # add factorial to total

print("Sum of series:", total)

#Note:Que a
#Outer for → runs from 1 to n
#1! = 1=1
#2! = 1*2 =2  
#3! = 1*2*3 =6
#4! = 1*2*3*4 =24
#5! = 1*2*3*4*5 =120


#b. N + N^2 + N^3+N^4 …..+N^N (here ^ means exponent)
N = int(input("Enter N: "))
total = 0
i = 1
while i <= N:
    total += N**i
    i += 1
print("Sum of series:", total)


#c. Find the sum of a geometric series from 1 to n where the common ratio is 2.
n = int(input("Enter number of terms: "))
total = 0
term = 1
i = 1
while i <= n:
    total += term
    term *= 2
    i += 1
print("Geometric Series Sum:", total)


#d. S = a + a2 / 2 + a3 / 3 + …… + a10 / 10
a = int(input("Enter value of a: "))
total = 0
i = 1
while i <= 10:
    total += (a**i) / i
    i += 1
print("Sum of series:", total)


#e. x - x2/3 + x3/5 - x4/7 + …. to n terms
x = int(input("Enter value of x: "))
n = int(input("Enter number : "))
total = 0
sign = 1
den = 1
i = 1

while i <= n:
    total += sign * (x**i) / den
    sign *= -1     # alternate + & -
    den += 2       # odd denominators
    i += 1

print("Sum of series:", total)
