# 8. Duplicate of list (not same reference)
li = [10, 20, 30]
dup = []
for i in li:
    dup.append(i)

print("Original =", li)
print("Duplicate =", dup)
