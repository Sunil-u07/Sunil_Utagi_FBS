# 9. Check palindrome
def palindrome(num):
    rev, temp = 0, num
    
    while temp > 0:
        digit = temp % 10
        rev = rev * 10 + digit
        temp //= 10
    return rev == num   

n = int(input("Enter number: "))
if palindrome(n):
    print(n, "is Palindrome")
else:
    print(n, "is Not Palindrome")

