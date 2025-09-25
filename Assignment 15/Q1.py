#Q1. Create a class Book with members as bid,bname,price and author.Add following methods: 
#a. Constructor (Support both parameterized and parameterless)  
#b. Destructor   
#c. ShowBook  

class Book:
    # Constructor (parameterized and parameterless)
    def __init__(self, bid=0, bname="Unknown", price=0.0, author="Unknown"):
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author
        print("Book object created")

    def __del__(self):
        print("Book object destroyed")

    def Show_book(self):
        print(f"Book ID: {self.bid}, Name: {self.bname}, Price: {self.price}, Author: {self.author}")


b1 = Book()  # parameterless
b1.Show_book()

b2 = Book(101, "Python Programming", 450, "Guido van Rossum")  # parameterized
b2.Show_book()
