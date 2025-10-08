#Q2. Create a derived class from Student as EnggStudent with : 
#a.  Data   members as :  
#i.  Branch 
#ii. InternalMarks 

#b.  Add the following methods : 
#i.  Parameterized constructor 
#ii. Display 
#iii. Accept 
#iv.  override Method CalculateRank 
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
      
        print(f"ID: {self.student_id}, Name: {self.name}, Age: {self.age}, Percentage: {self.percentage}, Rank: {self.calculateRank()}")

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
        # Overriding __str__ method
        return f"Student details\nID={self.student_id}\nName={self.name}\nAge={self.age}\nPercentage={self.percentage}\nRank={self.calculateRank()}"

# from Q1 import Student

# Derived class EnggStudent
class EnggStudent(Student):
    def __init__(self, student_id, name, age, percentage, branch, internal_marks):
        super().__init__(student_id, name, age, percentage)
        self.branch = branch
        self.internal_marks = internal_marks

    def calculateRank(self):
        final_score = (self.percentage + self.internal_marks) / 2
        if final_score >= 85:
            return "Excellent"
        elif final_score >= 65:
            return "Good"
        else:
            return "Average"

    def __str__(self):
        return f"EnggStudent details\nID={self.student_id}\nName={self.name}\nBranch={self.branch}\nInternalMarks={self.internal_marks}\nRank={self.calculateRank()}"

#Using accept()
e1=EnggStudent("", "", 0, 0, "", 0)
e1.accept()
print(e1)
print("----------------------------------")

#Using Parameterized()
e1 = EnggStudent("101", "Sneha", 21, 78, "Computer", 80)
print(e1)

