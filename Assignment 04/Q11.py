#Q11. check whether a number is strong number or not
import math

n = int(input("Enter a number: "))
temp = n
sum_fact = 0

while temp > 0:
    digit = temp % 10
    sum_fact += math.factorial(digit)   # direct factorial
    temp //= 10

if sum_fact == n:
    print("Strong Number")
else:
    print("Not Strong Number")

#Note:
#math.factorial :
#  1)built-in function in math module
#  2)Returns the factorial of a non-negative integer n.
