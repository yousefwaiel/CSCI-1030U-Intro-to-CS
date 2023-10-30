def get_class_average(marks):
    list_sum = sum(marks)
    list_count = len(marks)
    list_average = list_sum / list_count

    return list_average


midterm_marks = [57.0, 62.5, 68.0, 74.0, 55.0, 71.0, 94.5, 47.5]
midterm_average = get_class_average(midterm_marks)
print(f'{midterm_average = }') # 66.1875


