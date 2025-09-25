#Q12. print all armstrong numbers in a given range
start = int(input("Enter start: "))
end = int(input("Enter end: "))

for num in range(start, end+1):
    order = len(str(num))
    temp = num
    sum_pow = 0

    while temp > 0:
        digit = temp % 10
        sum_pow += digit ** order
        temp //= 10
        
    if sum_pow == num:
        print(num, end=" ")
 

