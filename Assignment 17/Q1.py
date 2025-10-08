#Q1. Create a class Student with following .
#a.  data members :   
#i.  StudentId 
#ii.  Name
#iii. Age
#iv.  Percentage

#b. Add the following methods : 
#i. Parameterized constructor 
#ii. Display 
#iii. Accept 
#iv   Method CalculateRank 
#v.   Override __str__ Method 


class Student:
    def __init__(self, student_id, name, age, percentage):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.percentage = percentage

    def accept(self):
        self.student_id = input("Enter Student ID: ")
        self.name = input("Enter Name: ")
        self.age = int(input("Enter Age: "))
        self.percentage = float(input("Enter Percentage: "))

    def display(self):
        print(f"ID: {self.student_id}\nName: {self.name}\nAge: {self.age}\nPercentage: {self.percentage}\nRank: {self.calculateRank()}")
        print("-------------------------------------------------")
        
    def calculateRank(self):
        #calculate rank
        if self.percentage >= 90:
            return "A+"
        elif self.percentage >= 75:
            return "A"
        elif self.percentage >= 60:
            return "B"
        else:
            return "C"

    def __str__(self):
        # Overriding __str__ ()
        return f"Student details\nID={self.student_id}\nName={self.name}\nAge={self.age}\nPercentage={self.percentage}\nRank={self.calculateRank()}"


s1 = Student("101", "Ravi", 20, 82.5) 
s1.display()                           
print(s1)                              
