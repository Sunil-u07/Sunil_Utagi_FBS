#Q8.Create a duplicate of an existing list. It should not point to same list.

li = [10, 20, 30]
dup = []
for i in li:
    dup.append(i)

print("Original =", li)
print("Duplicate =", dup)
