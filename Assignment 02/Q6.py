#Q6. Calculate total salary of employee based on basic, da=10% of basic, ta=12% of basic, hra=15% of basic.

basic = int(input("Enter basic salary: "))

da = 0.10 * basic
ta = 0.12 * basic
hra = 0.15 * basic

total_salary = basic + da + ta + hra
print("Total Salary =", total_salary)
