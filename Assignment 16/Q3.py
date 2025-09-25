#Q3. Create a class Shirt  with members as sid,sname,type(formal etc), price and # size(small,large etc) .Add following methods:  

# j. Constructor (Support both parameterized and parameterless)  
# k. Destructor   
# l. ShowBook  
# m. For each size of shirt price should change by 10%. 
# (eg. If 1000 is price then small price = 1000, medium = 1100,large=1200 and 
# xlarge=1300) Use static concept


class Shirt:
    size_price = {"Small": 0, "Medium": 10, "Large": 20, "XLarge": 30}  # Static: price increase %

    def __init__(self, sid=0, sname="Unknown", stype="Casual", price=0.0, size="Medium"):
        self.sid = sid
        self.sname = sname
        self.stype = stype
        self.base_price = price
        self.size = size
        self.price = price + (price * Shirt.size_price.get(size, 0) / 100) # price based on size
        print("Shirt object created")

    def show_shirt(self):
        print(f"Shirt ID: {self.sid}, Name: {self.sname}, Type: {self.stype}, Size: {self.size}, Price: {self.price}")

    @staticmethod
    def show_size_prices():  # Static method to show size price adjustment
        print("Size Price Adjustments (%):")
        for size, perc in Shirt.size_price.items():
            print(f"{size}: {perc}%")

    def __del__(self):
        print("Shirt object destroyed")
        

s1 = Shirt(301, "Allen Solly", "Formal", 1000, "Small")
s1.ShowBook()

s2 = Shirt(302, "Peter England", "Casual", 1000, "Medium")
s2.ShowBook()

s3 = Shirt(303, "Levis", "Formal", 1000, "Large")
s3.ShowBook()

s4 = Shirt(304, "UCB", "Casual", 1000, "XLarge")
s4.ShowBook()
