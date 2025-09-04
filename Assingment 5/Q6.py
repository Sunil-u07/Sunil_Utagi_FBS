for n in range(2, 101):
    is_prime = True
    i = 2
    while i*i <= n:
        if n % i == 0:
            is_prime = False
            break
        i += 1
    if is_prime:
        print(n, end=" ")
