p1 = int(input("Enter price of product 1: "))
p2 = int(input("Enter price of product 2: "))
p3 = int(input("Enter price of product 3: "))
p4 = int(input("Enter price of product 4: "))
p5 = int(input("Enter price of product 5: "))

total = p1 + p2 + p3 + p4 + p5

if total > 0:
    gst = total * 0.18
    final_amt = total + gst
    print("Total Price (without GST):", total)
    print("GST (18%):", gst)
    print("Final Amount :", final_amt)
else:
    print("Invalid total amount")