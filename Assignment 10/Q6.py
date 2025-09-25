#Q6. Remove duplicates from the list.
li = [1, 2, 2, 3, 4, 4, 5]
unique = []
for i in li:
    if i not in unique:
        unique.append(i)
print("Without Duplicates =", unique)
