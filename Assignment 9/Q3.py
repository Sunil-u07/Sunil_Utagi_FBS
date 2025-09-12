def reverse_no(num, rev=0):
    # Base case
    if num == 0:
        return rev
    # Recursive case
    return reverse_no(num // 10, rev * 10 + num % 10)

n = int(input("Enter number: "))
print("Reverse:", reverse_no(n))
