#Q3. Create a class Shirt  with members as sid,sname,type(formal etc), price and # size(small,large etc) . Add following methods: 
#g. Constructor (Support both parameterized and parameterless)  
#h. Destructor
#i. ShowBook  

class Shirt:
    def __init__(self, sid=0, sname="Unknown", stype="Casual", price=0.0, size="Medium"):
        self.sid = sid
        self.sname = sname
        self.stype = stype
        self.price = price
        self.size = size
        print("Shirt object created")

    def __del__(self):
        print("Shirt object destroyed")

    def Show_shirt(self):
        print(f"Shirt ID: {self.sid}, Name: {self.sname}, Type: {self.stype}, Price: {self.price}, Size: {self.size}")


s1 = Shirt()  # parameterless
s1.Show_shirt()

s2 = Shirt(301, "Allen Solly", "Formal", 1200, "Large")  # parameterized
s2.Show_shirt()
