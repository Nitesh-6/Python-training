class Mobiles:
    def __init__(self, brand, model, price, color, inStock):
        self.brand = brand
        self.model = model
        self.price = price
        self.color = color
        self.inStock = inStock

    def mobile_info(self):
        print("Mobile information:", self.brand, self.model, self.price, self.color, self.inStock)


gt_master = Mobiles("Realme", "Gt-Master", 21000.00, "gray", True)

gt_master.mobile_info()
