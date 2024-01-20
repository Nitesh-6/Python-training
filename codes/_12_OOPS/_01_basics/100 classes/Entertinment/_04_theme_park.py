class Theme_park:
    def __init__(self, name, address, price, no_rides):
        self.name = name
        self.address = address
        self.price = price
        self.no_rides = no_rides

    def theme_park_details(self):
        print("theme park details are:", self.name, self.address, self.price, self.no_rides)


mgm = Theme_park("MGM", "vizag", 400.00, 20)

mgm.theme_park_details()

