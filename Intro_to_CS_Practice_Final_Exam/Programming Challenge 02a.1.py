mid = float(input("Please insert your midterm mark out of 80 "))
lab = float(input("Please insert your Lab mark out of 30 "))
fin = float(input("Please insert your Final Exam mark out of 180 "))

mark = (mid / 80 * 30) + lab + (fin / 180 * 40)

print(f"Your Student's final mark is {mark}%")