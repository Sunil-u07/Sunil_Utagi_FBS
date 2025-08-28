# 12. Check 3 digit palindrome
num = int(input("Enter a 3-digit number: "))
first = num // 100        # first digit
last = num % 10           # last digit

if first == last:
    print("Palindrome")
else:
    print("Not Palindrome")
