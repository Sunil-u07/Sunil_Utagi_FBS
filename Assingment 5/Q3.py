passengers = int(input("Enter number of passengers: "))
ticket_cost = float(input("Enter ticket cost: "))
total_amount = 0

for i in range(1, passengers+1):
    age = int(input(f"Enter age of passenger {i}: "))
    if age < 12:
        total_amount += ticket_cost * 0.7   
    elif age > 59:
        total_amount += ticket_cost * 0.5   
    else:
        total_amount += ticket_cost        

print("Total Ticket Cost:", total_amount)
