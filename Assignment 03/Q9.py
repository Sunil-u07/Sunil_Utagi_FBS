#Q9. Display grade from 5 subject marks
marks = []
for i in range(5):
    marks.append(int(input(f"Enter marks of subject {i+1}: ")))
avg = sum(marks) / 5
if avg >= 60:
    print("First Class")
elif avg >= 50:
    print("Second Class")
elif avg >= 35:
    print("Pass Class")
else:
    print("Fail")


