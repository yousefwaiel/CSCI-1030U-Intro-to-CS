class Dog:
    def __init__(self,name, mass):
        self.name = name
        self.mass = mass

    def get_name(self):
        return self.name

    def set_name(self,name):
        self.name = name

    def __str__(self):
        return f'{self.name}({self.mass} kg)'

    def __lt__(self, other_cat):
        return self.mass < other_cat.mass

lenny = Dog('Lenny', 11.5)
print(f'{lenny.get_name() = }')
print(f'{str(lenny) = }')

boots = Dog('Boots', 7.4)
print(f'{boots < lenny = }')
