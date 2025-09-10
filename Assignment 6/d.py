# d) Alphabet pattern
for i in range(1, 6):
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()

#note: chr(65) = A, chr(66) = B, chr(67) = C and so on