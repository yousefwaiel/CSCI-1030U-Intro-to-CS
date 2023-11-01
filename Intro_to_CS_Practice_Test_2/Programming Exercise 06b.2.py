class Product:
    def __init__(self,price,description):
        self.price = price
        self.description = description

class Shoe(Product):
    def __init__(self,brand,size,color,price,description):
        super().__init__(price,description)
        self.brand = brand
        self.size = size
        self.color = color

    def __str__(self):
        return f'{self.brand} (price: {self.price}, colour: {self.color})'

products = [
    Shoe('Giovanna Barducci', 7.0, 'red', 39.99, 'high heel with strappy thing'),
    Shoe('Loic Montagne', 11.0, 'black', 99.99, 'pointy dress shoe'),
]
for product in products:
    print(str(product))