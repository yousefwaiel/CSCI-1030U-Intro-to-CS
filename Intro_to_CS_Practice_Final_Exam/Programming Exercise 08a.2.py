with open('midterm_marks_out.csv', 'r') as file:
    all_data = file.read()
    lines = all_data.split('\n')
    students = []
    for line in lines:
        if len(line) > 0:
            data = line.split(',')
            student = {
                'student_id': data[0].strip(),
                'midterm_mark': float(data[1]),
            }
            students.append(student)

print(f'{students = }')
