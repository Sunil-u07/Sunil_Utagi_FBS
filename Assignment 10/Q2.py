#2. Maximum and Minimum element
li = [7, 2, 9, 1, 5]
max = li[0]
min = li[0]

for i in li:
    if i > max:
        max = i
    if i < min:
        min = i

print("Maximum =", max)
print("Minimum =", min)
