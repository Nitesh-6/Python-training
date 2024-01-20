class Restaurant:
    def __init__(self, name, address, price, item):
        self.name = name
        self.address = address
        self.price = price
        self.item = item

    def get_restaurant_details(self):
        print("the details are:", self.name, self.address, self.price, self.item)


sai = Restaurant("sai", "vizag", 249.00, "Biryani")
sai.get_restaurant_details()
