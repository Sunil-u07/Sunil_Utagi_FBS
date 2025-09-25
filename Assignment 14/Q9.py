#Q9. Find all the unique combinations of 3 numbers from a given list of numbers, adding up to a target number.
from itertools import combinations

nums = [1,2,3,4,5]
target = 9

result = [combo for combo in combinations(nums, 3) if sum(combo) == target]
print("Combinations of 3 numbers adding to 9:", result)
