class Suppliers:
    def __init__(self, name, units_provided, input):
        self.name = name
        self.units_provided = units_provided
        self.input = input

    def suppliers_details(self):
        print("suppliers are:", self.name, self.units_provided, self.input)


ntpc = Suppliers("NTPC", "2200MW", 'coal')

ntpc.suppliers_details()