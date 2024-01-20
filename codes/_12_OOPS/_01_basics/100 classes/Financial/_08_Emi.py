class Emi:
    def __init__(self, name, amount, monthly_amount, is_paid):
        self.name = name
        self.amount = amount
        self.monthly_amount = monthly_amount
        self.is_paid = is_paid

    def get_emi_details(self):
        print("EMI details:", self.name, self.amount, self.monthly_amount, self.is_paid)


sai = Emi("sai", 2300.00, 383.33, True)

sai.get_emi_details()
