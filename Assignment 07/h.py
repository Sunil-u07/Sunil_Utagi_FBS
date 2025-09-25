#h)
k = 8  
for i in range(1, 6):
    # Left side incre no
    for j in range(1, i + 1):
        print(j, end=" ")
    
    # Middle spaces
    for j in range(1, k + 1):
        print(" ", end=" ")
    k -= 2  # reduce space for next row
    
    # Right side decre no
    for j in range(i, 0, -1):
        print(j, end=" ")
    
    print()

    #dont do this