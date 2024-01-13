class Telivision:
    def __init__(self, brand, inch, type, price):
        self.brand = brand
        self.inch = inch
        self.type  =type
        self.price = price

    def tv_details(self):
        print("TV details:", self.brand, self.inch, self.type, self.price)


mi = Telivision("mi", "55", "smart TV", "49999.00")

mi.tv_details()
