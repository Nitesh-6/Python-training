class Sellers:
    def __init__(self, name, address, products, quantity):
        self.name = name
        self.address = address
        self.products = products
        self.quantity = quantity

    def seller_info(self):
        print("seller information:", self.name, self.address, self.products, self.quantity)


sonic_soft = Sellers("sonic soft", "kurnool", "plastic granules", 250)

sonic_soft.seller_info()

