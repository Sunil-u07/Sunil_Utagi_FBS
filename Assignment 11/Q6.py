# 6. Find the Union of two Lists. 
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
union = []

for i in a:
    if i not in union:
        union.append(i)
for j in b:
    if j not in union:
        union.append(j)

print("Union =", union)
