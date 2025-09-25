#Q5.  Accept a number from user and check if this element is present in the list or not.Also tell how many times it is present in the list.
li = [4, 2, 7, 2, 9, 2]
x = int(input("Enter number: "))

count = 0
for i in li:
    if i == x:
        count += 1

if count > 0:
    print(x, "is present", count, "times")
else:
    print(x, "is not present")
