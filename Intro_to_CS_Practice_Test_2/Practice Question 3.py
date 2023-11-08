class Product:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def get_shipping_cost(self):
        return self.weight * 10

    def get_tax(self):
        return self.price * 0.13

    def get_total_cost(self):
        return self.price + self.get_tax() + self.get_shipping_cost()


razor = Product("Electric Razor", 49.99, 0.25)
homeGym = Product("Home Gym", 879.99, 115.0)
print("total cost of", razor.name, ":", razor.get_total_cost())
# 58.9887
print("total cost of", homeGym.name, ":", homeGym.get_total_cost())
