sids = ['100000000', '100000001', '100000002', '100000003', '100000004', '100000005', '100000006', '100000007',
        '100000008', '100000009']
midterm_marks = [52.0, 48.5, 54.25, 61.5, 64.0, 77.75, 29.0, 91.25, 68.25, 59.75]

with open('midterm_marks_out.csv', 'w') as file:
    for i in range(len(sids)):
        file.write(f'{sids[i]},{midterm_marks[i]}\n')

