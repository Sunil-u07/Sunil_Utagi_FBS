# c) Pascal's Triangle
for i in range(4):
    print(' ' * (3 - i), end='')   # 3 = rows-1
    num = 1
    
    for j in range(i + 1):
        print(num, end=' ')
        num = num * (i - j) // (j + 1)
    print()
