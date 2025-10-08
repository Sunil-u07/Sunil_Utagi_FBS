# Create a class MedicalStudent inherited from Student with following 
#i. Data members :Specialization 
#ii. MarksOfInternship 

#b. Add the following methods : 
#Data members :Specialization 
#MarksOfInternship

#b.Add the following methods : 
#i. Parameterized constructor 
#ii.Display 
#iii.Accept 
#iv. override Method CalculateRank
#v.  Override __str__ Method


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

    def calculateRank(self):

        if self.percentage >= 90:
            return "A+"
        elif self.percentage >= 75:
            return "A"
        elif self.percentage >= 60:
            return "B"
        else:
            return "C"

    def __str__(self):

        return f"Student details\nID={self.student_id}\nName={self.name}\nAge={self.age}\nPercentage={self.percentage}\nRank={self.calculateRank()}"

# from Q1 import Student

class MedicalStudent(Student):
    def __init__(self, student_id, name, age, percentage, specialization, internship_marks):
        super().__init__(student_id, name, age, percentage)
        self.specialization = specialization
        self.internship_marks = internship_marks

    def calculateRank(self):
        final_score = (self.percentage + self.internship_marks) / 2
        if final_score >= 85:
            return "Outstanding"
        elif final_score >= 65:
            return "Very Good"
        else:
            return "Needs Improvement"

    def __str__(self):
        return f"MedicalStudent details\nID={self.student_id}\nName={self.name}\n Specialization={self.specialization}\nInternshipMarks={self.internship_marks}\nRank={self.calculateRank()}"

#Using accept()
m1 = MedicalStudent("", "", 0, 0, "", 0)  
m1.accept()
print(m1)
print("----------------------------------")

#Using parameterized()
# m1 = MedicalStudent("201", "Amit", 22, 80, "Cardiology", 90)
# print(m1)   
