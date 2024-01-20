class Loan:
    def __init__(self, acc_no, loan_amount, loan_percent, interest):
        self.acc_no = acc_no
        self.loan_amount = loan_amount
        self.loan_percent = loan_percent
        self.interest = interest

    def get_loan_details(self):
        print("loan details:", self.acc_no, self.loan_amount, self.loan_percent, self.interest)


sai = Loan("12345678901", 1239.00, "10%", 123.00)

sai.get_loan_details()