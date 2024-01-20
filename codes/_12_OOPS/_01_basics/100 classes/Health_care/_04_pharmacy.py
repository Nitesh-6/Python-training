class Pharmacy:
    def __init__(self, name, id, location, employees, ):
        self.name = name
        self.id = id
        self.location = location
        self.employees = employees

    def get_pharmacy(self):
        print("details are: ", self.name, self.id, self.location, self.employees)


apollo = Pharmacy("Apollo", 6, "vizag", 4)
apollo.get_pharmacy()
