def main():
    # part 1

    defense = 5
    attack = 8
    hp = 10

    # TODO: YOUR CODE TO CALCULATE THE DAMAGE DONE GOES HERE

    if attack <= defense:
        print("No damage, since the defense stat is too high")
    else:
        damage = attack - defense
        hp = hp - damage
        print(f"{damage} damage inflicted, enemy HP is now {hp}")


    # part 2

    lab_mark = 9
    midterm_mark = 40
    final_exam_mark = 135

    # TODO: YOUR CODE TO CALCULATE THE STUDENT'S GRADE GOES HERE

    final_mark = ((lab_mark)*3) + ((midterm_mark) * 3/8) + ((final_exam_mark) / 4.5)

    grade = ""

    if final_mark < 50:
        grade = "F"
    elif final_mark < 60:
        grade = "D"
    elif final_mark < 70:
        grade = "C"
    elif final_mark < 80 :
        grade = "B"
    else:
        grade = "A"

    print(f"This students final grade is {grade}.")

if __name__ == "__main__":
    main()