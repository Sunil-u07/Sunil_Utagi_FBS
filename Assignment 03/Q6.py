#Q6. Calculate profit or loss. 
cp = int(input("Enter cost price: "))
sp = int(input("Enter selling price: "))

if sp > cp:
    print("Profit:", sp - cp)
elif sp < cp:
    print("Loss:", cp - sp)
else:
    print("No profit, no loss.")

