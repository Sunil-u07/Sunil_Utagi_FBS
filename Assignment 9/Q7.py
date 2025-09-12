def sum_digits(num):
    if num == 0:               
        return 0
    digit = num % 10           
    return digit + sum_digits(num // 10)

n = int(input("Enter number: "))
print("Sum of digits:", sum_digits(n))
