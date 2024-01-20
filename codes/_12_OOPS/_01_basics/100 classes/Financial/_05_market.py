class Market:
    def __init__(self, name, location, time_zone, num_of_emp):
        self.name = name
        self.location = location
        self.time_zone = time_zone
        self.num_of_emp = num_of_emp

    def get_market_details(self):
        print("market details", self.name, self.location, self.time_zone, self.num_of_emp)


bse = Market("BSE", "Mumbai", "+5:30", 200)

bse.get_market_details()
