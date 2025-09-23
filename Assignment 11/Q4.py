# 4. Second largest number using Bubble Sort
li = [10, 40, 20, 50, 30]

# bubble sort ascending
for i in range(len(li)):
    for j in range(len(li)-1):
        if li[j] > li[j+1]:
            li[j], li[j+1] = li[j+1], li[j]

print("Second Largest =", li[-2])
