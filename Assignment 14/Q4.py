#Q4. Finds all pairs of elements in a list whose sum is equal to a given value.

lst = [1,2,3,4,5]
target = 5
pairs = {(x, y) for x in lst for y in lst if x < y and x + y == target}
print("Pairs with sum 5:", pairs)
