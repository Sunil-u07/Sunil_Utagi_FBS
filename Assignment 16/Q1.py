#Q1. Create a class Book with members as bid,bname,price and author.Add following # methods:  

#a. Constructor (Support both parameterized and parameterless)  
#b. Destructor   
#c. ShowBook  
#d. Add static variable count and also maintain count of objects created.
 
class Book:
    count = 0  # static variable to track obj

    def __init__(self, bid=0, bname="Unknown", price=0.0, author="Unknown"):
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author
        Book.count += 1
        print('Constructor is called...')

    def show_book(self):
        return f'ID: {self.bid}, Name: {self.bname}, Price: {self.price}, Author: {self.author}'

    @staticmethod
    def show_count():  # Static method to show obj count
        print(f"Total Books Created: {Book.count}")

    def __del__(self):
        print("Destructor is called...")

b1 = Book()
print(b1.show_book())
b2 = Book(101, "Modi 3.0", 550, "Saurav Patil")
print(b2.show_book())
print("Total Books Created:", Book.count)
