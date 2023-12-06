names = ['Lucie Manette', 'Charles Darnay', 'Sydney Carton']
test1_marks = [34.0, 75.5, 58.0]
test2_marks = [47.5, 82.0, 63.5]
student_data = []

for i in range(len(names)):
    fullName = names[i].split()
    firstName = fullName[0]
    lastName = fullName[1]

    student_data.append({
        'first_name': firstName,
        'last_name': lastName,
        'test1': test1_marks[i],
        'test2': test2_marks[i],
    })

if student_data:
        del student_data[-1]

print(student_data)


#part 2

character = {
        'name': 'Grimbor',
        'race': 'Dwarf',
        'class': 'Warrior',
        'hp': 58,
        'level': 9,
    }


name = character['name']
level = character['level']
race = character['race']
char_class = character['class']
hp = character['hp']

print(f'{name} (level {level} {race} {char_class}) - HP: {hp}')