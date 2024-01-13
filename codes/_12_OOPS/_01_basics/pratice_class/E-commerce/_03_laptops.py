class Laptop:
    def __init__(self, brand, model, price, inStock):
        self.brand = brand
        self.model = model
        self.price = price
        self.inStock = inStock

    def laptop_info(self):
        print("laptop information:", self.brand, self.model, self.price, self.inStock)


ideapad3 = Laptop("Lenovo", "Idea pad-3", 50000.00, True)

ideapad3.laptop_info()

