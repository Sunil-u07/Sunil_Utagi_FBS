# 2. Merge two lists and sort
a = [5, 1, 9]
b = [8, 3, 2]
merged = []

# merge
for i in a:
    merged.append(i)
for j in b:
    merged.append(j)

# bubble sort
for i in range(len(merged)):
    for j in range(len(merged)-1):
        if merged[j] > merged[j+1]:
            merged[j], merged[j+1] = merged[j+1], merged[j]

print("Merged & Sorted List =", merged)
