#Q3. Second largest element in the list.
li = [10, 25, 5, 30, 20]
first = second = li[0]

for i in li:
    if i > first:
        second = first
        first = i
    elif i > second and i != first:
        second = i

print("Second Largest =", second)
