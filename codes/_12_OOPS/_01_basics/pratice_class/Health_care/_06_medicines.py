class Medicines:
    def __init__(self, name, used_for, price, mfd_date, exp_date):
        self.name = name
        self.used_for = used_for
        self.price = price
        self.mfd_date = mfd_date
        self.exp_date = exp_date

    def medicines_details(self):
        print("the medicines are: ", self.name, self.used_for, self.price, self.mfd_date, self.exp_date)


dolo = Medicines("Dolo", "fever", "30.56", "06-03-2023", "06-03-2024")
dolo.medicines_details()
