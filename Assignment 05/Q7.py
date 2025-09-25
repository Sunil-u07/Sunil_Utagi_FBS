#Q7. Print first n prime numbers
n = int(input("Enter how many prime numbers you want: "))

count = 0   
num = 2     
while count < n:
    i = 2
    prime = True
    while i * i <= num:
        if num % i == 0:
            is_prime = False
            break
        i += 1
    if prime:
        print(num, end=" ")
        count += 1
    num += 1
