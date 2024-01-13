class Cloths:
    def __init__(self, category, gender, size, price):
        self.category = category
        self.gender = gender
        self.size = size
        self.price = price

    def cloths_data(self):
        print("cloths are:", self.category, self.gender, self.size, self.price)


shirts = Cloths("shirts", "male", "xxl", 999.0)

shirts.cloths_data()