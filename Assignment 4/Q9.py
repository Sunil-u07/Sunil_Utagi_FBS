start = int(input("Enter start: "))
end = int(input("Enter end: "))
divisor = int(input("Enter divisor: "))

for i in range(start, end+1):
    if i % divisor == 0:
        print(i, end=" ")
