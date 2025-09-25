#Q1. Login system with 3 attempts
userid = "admin"
password = "1234"

for attempt in range(3):
    u = input("Enter User ID: ")
    p = input("Enter Password: ")
    if u == userid and p == password:
        print("Login Successful")
        break
    else:
        print("Invalid Credentials")
else:
    print("3 Attempts Over")
