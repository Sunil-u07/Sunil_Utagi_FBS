n = int(input("Enter a number: "))
temp = n
sum_fact = 0

while temp > 0:
    digit = temp % 10
    fact = 1
    j = 1
    while j <= digit:
        fact *= j
        j += 1
    sum_fact += fact
    temp //= 10

if sum_fact == n:
    print("Strong Number")
else:
    print("Not Strong Number")
