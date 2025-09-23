# 3. Sort list by second element in sublist
li = [[1, 5], [2, 3], [4, 1], [6, 2]]

# bubble sort based on second ele
for i in range(len(li)):
    for j in range(len(li)-1):
        if li[j][1] > li[j+1][1]:
            li[j], li[j+1] = li[j+1], li[j]

print("Sorted by second element =", li)
