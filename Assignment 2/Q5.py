#Q5. Selling Price with Discount
cost_price = int(input("Enter cost price of book: "))
discount = int(input("Enter discount percentage: "))

selling_price = cost_price - (cost_price * discount / 100)
print("Selling Price =", selling_price)
