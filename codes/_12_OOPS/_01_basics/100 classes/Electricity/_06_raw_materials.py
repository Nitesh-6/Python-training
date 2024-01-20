class Raw_materials:
    def __init__(self, name, efficiency, inp_cost, price):
        self.name = name,
        self.efficiency = efficiency
        self.inp_cost = inp_cost
        self.price = price

    def raw_details(self):
        print("raw materials details:", self.name, self.efficiency, self.inp_cost, self.price)


coal = Raw_materials("coal", "79%", "4.09", "6.03")
coal.raw_details()
