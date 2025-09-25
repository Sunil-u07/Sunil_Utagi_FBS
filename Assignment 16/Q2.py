#Q2. Create a class Product with members as pid,pname,price and quantity .Add following methods: 

#e. Constructor (Support both parameterized and parameterless)  
#f. Destructor   
#g. ShowBook  
#h. Add static member discount.  
#i. Provide methods for applying discount on price of product.

class Product:
    discount = 10  # static variable: discount %

    def __init__(self, pid=0, pname="Unknown", price=0.0, quantity=0):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity
        print('Constructor is called...')

    def show_product(self):
        return f'ID: {self.pid}, Name: {self.pname}, Price: {self.price}, Quantity: {self.quantity}'

    def apply_discount(self):
        discounted_price = self.price - (self.price * Product.discount / 100)
        return f"Original Price: {self.price}, Discounted Price: {discounted_price}"

    @staticmethod
    def change_discount(new_discount):  # Static method to change discount
        Product.discount = new_discount
        print(f"Discount changed to {Product.discount}%")

    def __del__(self):
        print("Destructor is called...")


P1 = Product(101, "Chair", 250, 10)
print(P1.show_Product())
print(P1.apply_discount())
