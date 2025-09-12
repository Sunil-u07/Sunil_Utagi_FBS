#check armstrong number or not using recursion
def armstrong(num):
    if num == 0:
        return 0
    else:
        digit = num % 10
        return digit ** len(str(n)) + armstrong(num // 10)

n = int(input("Enter number: "))

if n == armstrong(n):
    print(f"{n} is an Armstrong Number")
else:
    print(f"{n} is Not an Armstrong Number")