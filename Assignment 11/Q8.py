# 8. Snakes and ladder pattern (1–100 zig-zag)
n = 10
num = 1
for row in range(n):
    line = []
    for col in range(n):
        line.append(num)
        num += 1
    if row % 2 == 0:
        print(line)       # left to right
    else:
        print(line[::-1]) # right to left
