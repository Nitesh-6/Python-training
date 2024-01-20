class Loans:
    def __init__(self, name, type_of_loan, period, id):
        self.name = name
        self.type_of_loan = type_of_loan
        self.period = period
        self.id = id

    def get_loan_details(self):
        print("Loan details:", self.name, self.type_of_loan, self.period, self.id)


sai = Loans("sai", "bike", "12 months", 6)

sai.get_loan_details()
