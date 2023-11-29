class Dog:

    def __init__(self, name, mass):
        self.__name = name
        self.__mass = mass

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def __str__(self):
        return f'{self.__name} ({self.__mass} kg)'

    def __lt__(self, other_cat):
        return self.__mass < other_cat.__mass


lenny = Dog('Lenny', 11.5)
print(f'{lenny.get_name() = }')
print(f'{str(lenny) = }')

boots = Dog('Boots', 7.4)
print(f'{boots < lenny = }')