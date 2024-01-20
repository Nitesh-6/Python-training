class Appointment:
    def __init__(self, name, appointment_type, doc_name, bill):
        self.name = name
        self.appointment_type = appointment_type
        self.doc_name = doc_name
        self.bill = bill

    def appointment_details(self):
        print("The appointment details are: ", self.name, self.appointment_type, self.doc_name, self.bill)


sai = Appointment("sai", "consultation", "Nitesh", 250.0)
sai.appointment_details()
