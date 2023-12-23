def main():
    # part 1

    defense = 5
    attack = 8
    hp = 10

    if attack<= defense:
        print("No damage, since the defense stat is too high")
    else :
        damage = attack - defense
        hp -= damage
        print(f'{damage} damage inflected, enemy HP is now {hp}')

    # part 2

    labMark = float(9)
    midtermMark = float(40)
    finalExamMark = float(135)

    finalMark = labMark*3 + midtermMark/(80/30) + finalExamMark/(180/40)


    if finalMark<50:
        print(f'This students final grade is F')
    elif finalMark <60:
        print(f'This students final grade is D')
    elif finalMark < 70:
        print(f'This students final grade is C')
    elif finalMark < 80:
        print(f'This students final grade is B')
    else:
        print(f'This students final grade is A')








if __name__ == "__main__":
    main()