def main():
    # part 1

    names = ['Lucie Manette', 'Charles Darnay', 'Sydney Carton']
    test1_marks = [34.0, 75.5, 58.0]
    test2_marks = [47.5, 82.0, 63.5]

    student_data = []

    # TODO: YOUR CODE TO CREATE THE LIST OF DICTIONARIES GOES HERE

    data = {}

    for n in range(len(names)):
        full_name = names[n].split(" ")
        first_name = full_name[0]
        last_name = full_name[1]

        student_data.append({
            "first_name": first_name,
            "last_name": last_name,
            "test1": test1_marks[n],
            "test2": test2_marks[n],
        })

    # TODO: YOUR CODE TO DELETE THE LAST CHARACTER GOES HERE

    if student_data:
        del student_data[-1]

    print(student_data)

    # part 2

    character = {
        'name': 'Grimbor',
        'race': 'Dwarf',
        'class': 'Warrior',
        'hp': 58,
        'level': 9,
    }

    # TODO: YOUR CODE TO OUTPUT A SUMMARY FOR THIS CHARACTER GOES HERE

    print(f"{character['name']} ( level {character['level']} {character['race']} {character['class']} - HP: {character['hp']} )")

if __name__ == "__main__":
    main()
