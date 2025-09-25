#Q10. check whether a number is perfect number or not
n = int(input("Enter a number: "))
sum_div = 0

i = 1
while i < n:
    if n % i == 0:
        sum_div += i
    i += 1

if sum_div == n:
    print("Perfect Number")
else:
    print("Not Perfect Number")

