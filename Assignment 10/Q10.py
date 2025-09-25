#Q10. Remove all occurrences of given element in the list.
li = [1, 2, 3, 2, 4, 2, 5]
x = int(input("Enter element to remove: "))
result = []
for i in li:
    if i != x:
        result.append(i)
print("List after removal =", result)
