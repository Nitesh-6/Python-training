class Patients:
    def __init__(self, id, name, health_issue, bill):
        self.id = id
        self.name = name
        self.health_issue = health_issue
        self.bill = bill

    def get_patient_details(self):
        print("patient details are:", self.id, self.name, self.health_issue, self.bill)


sai = Patients(1, "sai", "fever", 250.0)
sai.get_patient_details()
