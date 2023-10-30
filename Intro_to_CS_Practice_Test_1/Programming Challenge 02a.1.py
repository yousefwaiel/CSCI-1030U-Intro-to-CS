midtermMark = int(input("Please insert your midterm mark out of 80"))
labMark = int(input("Please insert your lab mark out of 30"))
finalExamMark = int(input("Please insert your final exam mark out of 180"))

finalMark = (midtermMark / 80*30) + labMark + (finalExamMark / 180*40 )

print("The Students final mark out of 100 is", finalMark)