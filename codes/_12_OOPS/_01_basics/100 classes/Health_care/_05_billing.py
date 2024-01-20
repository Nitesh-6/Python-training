class Billing:
    def __init__(self, id, name, age, bill_amt, payment_status):
        self.id = id
        self.name = name
        self.age = age
        self.bill_amt = bill_amt
        self.payment_status = payment_status

    def bill_details(self):
        print("The bill details are: ", self.id, self.name, self.age, self.bill_amt, self.payment_status)


sai = Billing(6, "sai", 24, 320.50, True)
sai.bill_details()
