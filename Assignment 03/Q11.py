#Q11. Accept age of five people and also per person ticket amount and then calculate total 
# amount to ticket to travel for all of them based on following condition : 

# a. Children below 12 = 30% discount 
# b. Senior citizen (above 59) = 50% discount 
# c. Others need to pay full. 


total = 0
for i in range(5):
    age = int(input(f"Enter age of person {i+1}: "))
    ticket = float(input("Enter ticket amount: "))
    if age < 12:
        cost = total + ticket * 0.7   # 30% discount
    elif age > 59:
        cost = total + ticket * 0.5   # 50% discount
    else:
        cost = total + ticket         # full price

print(f"Total Ticket Amount = {cost}")
