#Student Marks & Percentage
num_students = int(input("Enter number of students: "))
all_per = []

for i in range(num_students):
    print(f"\nStudent {i+1}:")
    total = 0
    for j in range(5):
        marks = int(input(f"Enter marks for subject {j+1}: "))
        total += marks
    percentage = total / 5
    all_per.append(percentage)
    print("Percentage:", percentage)

avg_per = sum(all_per) / num_students
print("All Percentages:", all_per)
print("Average Percentage:", avg_per)
