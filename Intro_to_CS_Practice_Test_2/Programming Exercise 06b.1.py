class Pet:
    def __init__(self,name,breed,mass,sex):
        self.name = name
        self.breed = breed
        self.mass = mass
        self.sex = sex
class Dog(Pet):
    def speak(self):
        print(f'{self.name}: woof')

class Cat(Pet):
    def speak(self):
        print(f'{self.name}: meow')

class Robot:
    def speak(self):
        print("Beep Beep Boop")


pets = [
    Dog('Keva', 'Sheepadoodle', 15.0, 'female'),
    Cat('Lenny', 'Long Hair Domestic', 9.2, 'male'),
    Robot(),
]


for pet in pets:
    pet.speak()