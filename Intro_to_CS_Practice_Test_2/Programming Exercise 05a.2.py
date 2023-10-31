def myfilter(check, values):
    output = []
    for i in values:
        if check(i):
            output.append(i)
    return output

marks = [64.5, 87.0, 55.5, 94.0, 71.5, 46.0, 100.0]
a_grades = myfilter(lambda mark: mark > 80.0, marks)
print(a_grades)