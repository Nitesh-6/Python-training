class Supply:
    def __init__(self, id, type, price, tax):
        self.id = id
        self.type = type
        self.price = price
        self.tax = tax

    def supply_info(self):
        print("supply details are:", self.id, self.type, self.price, self.tax)


commercial = Supply(123, "commercial", "12/unit", "15%")
commercial.supply_info()

