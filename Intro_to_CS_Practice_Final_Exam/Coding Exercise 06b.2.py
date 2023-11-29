class Product:
    def __init__(self, price, description):
        self._price = price
        self._description = description


class Shoe(Product):
    def __init__(self, brand, size, colour, price, description):
        super().__init__(price, description)
        self._brand = brand
        self._size = size
        self._colour = colour

    def __str__(self):
        return f'{self._brand} (price: {self._price}, colour: {self._colour})'


products = [
    Shoe('Giovanna Barducci', 7.0, 'red', 39.99, 'high heel with strappy thing'),
    Shoe('Loic Montagne', 11.0, 'black', 99.99, 'pointy dress shoe'),
]
for product in products:
    print(str(product))
