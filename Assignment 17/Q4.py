#Q4. Create a class College which has collection of students. Add the # following methods : 

#a. Parameteried constructor for number of students. 
#b. AddStudent 
#c. GetStudent 
#d. RemoveStudent 
#e. Override __str__ Method

class College:
    def __init__(self, no_of_students):
        self.no_of_students = no_of_students
        self.students = []  

    def addStudent(self, student):
        if len(self.students) < self.no_of_students:
            self.students.append(student)
            print(f"Student {student.name} added successfully.")
        else:
            print("Cannot add more students, limit reached.")

    def getStudent(self, student_id):
        for s in self.students:
            if s.student_id == student_id:
                return s
        return None

    def removeStudent(self, student_id):
        for s in self.students:
            if s.student_id == student_id:
                self.students.remove(s)
                print(f"Student {s.name} removed successfully.")
                return
        print("Student not found!")

    def displayAll(self):
        print("\n--- College Students ---")
        for s in self.students:
            print(s)

    def __str__(self):
        return f"College with {len(self.students)}/{self.no_of_students} students."


# Reusing Student class from Q1
class Student:
    def __init__(self, student_id, name, age, percentage):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.percentage = percentage

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
        return f"Student[ID={self.student_id}, Name={self.name}, Age={self.age}, Percentage={self.percentage}, Rank={self.calculateRank()}]"


# Create college for 3 students
college = College(3)

# Add students
s1 = Student("101", "Ravi", 20, 82.5)
s2 = Student("102", "Meena", 21, 91.0)
s3 = Student("103", "Karan", 19, 67.0)

college.addStudent(s1)
college.addStudent(s2)
college.addStudent(s3)


college.displayAll()


print("\nGet Student 102:")
print(college.getStudent("102"))

college.removeStudent("101")
college.displayAll()
print(college)

