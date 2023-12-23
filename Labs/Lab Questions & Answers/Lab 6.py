import math


# part 1,2,3

class Shapes:
    def __init__(self):
        pass
class Rectangle(Shapes):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self, width, height):
        area = width * height
        return area

    def get_perimeter(self, width, height):
        perimeter = width * 2 + height * 2


class Circle(Shapes):

    def __init__(self, radius):
        self.radius = radius

    def get_area(self, radius):
        area = math.pi * radius
        return area

    def get_perimeter(self, radius):
        perimeter = 2 * math.pi * radius
        return perimeter

