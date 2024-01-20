class Injuries:
    def __init__(self, name, preferspecialist, medicine_used, hospitals):
        self.preferspecialist = preferspecialist
        self.name = name
        self.medine_used = medicine_used
        self.hospitals = hospitals

    def injury_details(self):
        print("The injuries are: ", self.name, self.preferspecialist, self.medine_used, self.hospitals)


burn = Injuries("Burn", "Dermatologist", "petroleum", "skin plus")
burn.injury_details()
