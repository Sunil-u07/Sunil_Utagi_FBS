# Check Leap year or Not
def leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

year = int(input("Enter year: "))
if leap_year(year):
    print(f"{year} is a Leap Year")
else:
    print(f"{year} is Not a Leap Year")
