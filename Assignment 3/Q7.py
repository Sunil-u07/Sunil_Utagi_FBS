# 7. Check if user has entered correct userid and password
userid = "admin"
password = "1234"

u = input("Enter userid: ")
p = input("Enter password: ")
if u == userid and p == password:
    print("Login Successful")
else:
    print("Invalid Credentials")
