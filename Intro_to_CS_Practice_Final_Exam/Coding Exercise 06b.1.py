class Pet:
    def __init__(self, name, breed, age, gender):
        Pet.__name = name
        Pet.__age = age
        Pet.__gender = gender

    def Speak(self):
        print("sound")


class Dog(Pet):
    def Speak(self):
        print("Woof")


class Cat(Pet):
    def Speak(self):
        print("Meow")



pets = [
  Dog('Rufus', 'Husky', 8.0, 'female'),
  Cat('Boots', 'Long hair', 3.2, 'male')
]
for pet in pets:
  pet.Speak()
