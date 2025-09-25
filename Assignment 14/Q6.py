#Q6.  find the two numbers whose product is maximum among all the pairs in a given list of numbers.
nums = [1,3,5,2,4]
max_product = max({(x,y) for x in nums for y in nums if x != y}, key=lambda t: t[0]*t[1])
print("Pair with max product:", max_product)
