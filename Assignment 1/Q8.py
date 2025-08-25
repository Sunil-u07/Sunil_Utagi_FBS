#Q8. Convert days
days = int(input("Enter number of days: "))
years = days // 365
weeks = (days % 365) // 7
remaining_days = (days % 365) % 7
print("Years:", years, "Weeks:", weeks, "Days:", remaining_days)