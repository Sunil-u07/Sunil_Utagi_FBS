# 6. Remove duplicates
li = [1, 2, 2, 3, 4, 4, 5]
unique = []
for i in li:
    if i not in unique:
        unique.append(i)
print("Without Duplicates =", unique)
