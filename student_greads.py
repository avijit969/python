student_marks = {'avijit': 98, 'abhishek': 99, 'disha': 69, 'kedar': 85}
student_greads = {}
for student in student_marks:
    mark = student_marks[student]
    if mark > 90:
        student_greads[student] = 'A+'
    elif mark > 80:
        student_greads[student] = 'A'
    elif mark > 70:
        student_greads[student] = 'B'
    elif mark > 60:
        student_greads[student] = 'C'
    elif mark > 50:
        student_greads[student] = 'D'
    elif mark > 40:
        student_greads[student] = 'E'
    else:
        student_greads[student] = 'F'

print(student_greads)
