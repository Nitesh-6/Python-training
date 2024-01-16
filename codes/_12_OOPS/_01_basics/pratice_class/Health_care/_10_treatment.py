class Treatment:
    def __init__(self, injury_type, treatment_used, doc_name, bill, medicine):
        self.injury_type = injury_type
        self.treatment_used = treatment_used
        self.doc_name = doc_name
        self.bill = bill
        self.medicine = medicine

    def treatment_details(self):
        print("The treatment details: ", self.injury_type, self.treatment_used, self.doc_name, self.bill, self.medicine)


fracture = Treatment("Fracture", "Surgery", "Nitesh", 15000.0, "plaster cast")
fracture.treatment_details()
