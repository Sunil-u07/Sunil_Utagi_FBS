# 1. Even and Odd elements into two lists
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
