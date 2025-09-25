#Q1. Even and Odd elements of a List into two Different Lists.
li = [1, 2, 3, 4, 5, 6, 7, 8]
even = []
odd = []
for i in li:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print("Even List =", even)
print("Odd List =", odd)
