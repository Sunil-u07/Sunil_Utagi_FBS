#Q13. Print list after removing even numbers.
li = [1, 2, 3, 4, 5, 6, 7]
result = []
for i in li:
    if i % 2 != 0:
        result.append(i)
print("After removing evens =", result)
 