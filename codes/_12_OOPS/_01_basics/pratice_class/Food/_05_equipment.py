class Equipment:
    def __init__(self, name, cost, used_for):
        self.name = name
        self.cost = cost
        self.used_for = used_for

    def get_equipment_details(self):
        print("equipment details are:", self.name, self.cost, self.used_for)

lighter = Equipment("lighter", 50.0, "to put fire")
lighter.get_equipment_details()