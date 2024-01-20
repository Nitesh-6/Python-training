class Generators:
    def __init__(self, brand, type, power, fuel_used):
        self.brand = brand
        self.type = type
        self.power = power
        self.fuel_used = fuel_used

    def generator_details(self):
        print("generator details", self.brand, self.type, self.power, self.fuel_used)


ss_gold = Generators("ss-Gold", "semi-silent", 87000, "Diesel")

ss_gold.generator_details()
