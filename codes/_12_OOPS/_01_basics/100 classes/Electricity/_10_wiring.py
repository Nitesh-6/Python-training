class Wiring:
    def __init__(self, brand, type, price):
        self.brand = brand
        self.type =type
        self.price = price

    def wiring_details(self):
        print("wiring Details:", self.brand, self.type, self.price)


polycab = Wiring("polycab", "AC", "20/mtr")

polycab.wiring_details()
