# 4. Reverse the list
li = [1, 2, 3, 4, 5]
rev = []
for i in range(len(li)-1, -1, -1):
    rev.append(li[i])
print("Reversed List =", rev)
