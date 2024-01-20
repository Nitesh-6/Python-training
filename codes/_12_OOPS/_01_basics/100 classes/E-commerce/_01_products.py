class Products:
    def __init__(self, product_num, category, name, price):
        self.product_num = product_num
        self.category = category
        self.name = name
        self.price = price

    def get_products(self):
        print("products are:", self.product_num, self.category, self.name, self.price)


realme = Products(1, "mobile", "Realme", 21000.00)

realme.get_products()
