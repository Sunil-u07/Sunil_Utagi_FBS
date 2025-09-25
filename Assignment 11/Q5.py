#Q5. Sort a List According to the Length of the Elements.
li = ["apple", "kiwi", "banana", "orange", "grapes"]

# bubble sort by length
for i in range(len(li)):
    for j in range(len(li)-1):
        if len(li[j]) > len(li[j+1]):
            li[j], li[j+1] = li[j+1], li[j]

print("Sorted by length =", li)
