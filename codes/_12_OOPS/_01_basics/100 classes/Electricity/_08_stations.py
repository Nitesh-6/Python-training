class Stations:
    def __init__(self, location, price, num_of_emp, units_generated):
        self.location = location
        self.price = price
        self.num_of_emp = num_of_emp
        self.units_generated = units_generated

    def station_det(self):
        print("station details are:", self.location, self.price, self.num_of_emp, self.units_generated)


vizag = Stations("vizag", 3.09, 30, "10000MW")

vizag.station_det()
