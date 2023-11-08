class Student_Entry:
    def __init__(self, name, sid):
        self.labs = 0.0
        self.assignments = 0.0
        self.midterm = 0.0
        self.final = 0.0
        self.name = name
        self.sid = sid

    def get_average(self):
        return self.assignments + self.labs + (self.midterm * 0.3 ) + (self.final * 0.4)

    def letter_grade(self):
        if self.get_average() <= 49:
            return "F"
        elif self.get_average() <= 59:
            return "D"
        elif self.get_average() <= 69:
            return "C"
        elif self.get_average() <= 79:
            return "B"
        else:
            return "A"

    def __lt__(self, other):
        return self.get_average() < other.get_average()


bsmith = Student_Entry("Bob Smith", "1000001")
bsmith.labs = 9.0
bsmith.assignments = 17.0
bsmith.midterm = 57.5
bsmith.final = 60.0
print("Bob Smith: ", bsmith.letter_grade())
# C
sjones = Student_Entry("Sally Jones", "1000002")
sjones.labs = 9.5
sjones.assignments = 19.5
sjones.midterm = 81.0
sjones.final = 74.5
print("Sally Jones: ", sjones.letter_grade())