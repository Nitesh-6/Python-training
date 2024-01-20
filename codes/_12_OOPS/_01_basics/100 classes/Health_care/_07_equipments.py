class Equipments:
    def __init__(self, name, used_for, qty, price):
        self.name = name
        self.used_for = used_for
        self.qty = qty
        self.price = price

    def equipment_details(self):
        print("The equipments are: ", self.name, self.used_for, self.qty, self.price)


thermometer = Equipments("Thermometer", "checking temperature", 4, 180.0)
thermometer.equipment_details()
