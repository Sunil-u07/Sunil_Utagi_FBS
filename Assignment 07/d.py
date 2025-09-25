#d) Number Pyramid Pattern
n = 5
for i in range(1, n+1):
    # Spaces
    print("  " * (n-i), end="")

    # Increasing 
    for j in range(i, 2*i):
        print(j, end="")
        print(" ", end="")

    # Decreasing 
    for j in range(2*i-2, i-1, -1):
        print(j, end=" ")
    print()

# dont do this 