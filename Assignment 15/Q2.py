#Q2. Create a class Product with members as pid,pname,price and quantity .Add following methods: 
#d. Constructor (Support both parameterized and parameterless)  
#e. Destructor   
#f. ShowBook  

class Product:
    def __init__(self, pid=0, pname="Unknown", price=0.0, quantity=0):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity
        print("Product object created")

    def __del__(self):
        print("Product object destroyed")

    def Show_product(self):
        print(f"Product ID: {self.pid}, Name: {self.pname}, Price: {self.price}, Quantity: {self.quantity}")


p1 = Product()  # parameterless
p1.Show_product()

p2 = Product(201, "Laptop", 55000, 10)  # parameterized
p2.Show_product()
