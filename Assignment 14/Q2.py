#Q2. Remove intersection of a second set from the first set.
a = {1,2,3,4,5}
b = {4,5,6,7}
a.difference_update(b)
print("First set after removing intersection:", a)  # {1,2,3}
