class Atm:
    def __init__(self, bank_name, branch, location, amount_limit):
        self.bank_name = bank_name
        self.branch = branch
        self.location = location
        self.amount_limit = amount_limit

    def get_atm_details(self):
        print("ATM details are:", self.bank_name, self.branch, self.location, self.amount_limit)


kommadi = Atm("HDFC", "kommadi", "vizag", 320000.00)

kommadi.get_atm_details()
