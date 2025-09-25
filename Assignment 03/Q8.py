#Q8. User login with captcha
import random

userid = "sunil"
password = "1234"

u = input("Enter userid: ")
p = input("Enter password: ")

if u == userid and p == password:
    captcha = str(random.randint(1000, 9999))
    print("Captcha:", captcha)
    c = input("Enter the captcha: ")
    if c == captcha:
        print("Login Successful")
    else:
        print("Captcha Incorrect. Login Failed.")
else:
    print("Invalid Credentials")
    


    # Note :(IMPORTANT)
    #import string

    # Generate a 4-character alphanumeric captcha :
    # captcha = ''.join(random.choices(string.ascii_letters + string.digits, k=4))