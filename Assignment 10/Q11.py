# 11. Numbers divisible by m and n
li = [10, 20, 30, 40, 50, 60]
m = 2
n = 5
for i in li:
    if i % m == 0 and i % n == 0:
        print(i, end=" ")
