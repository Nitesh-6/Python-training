class Transaction:
    def __init__(self, accc_num, ifsc_code, amount, status):
        self.acc_num = accc_num
        self.ifsc_code = ifsc_code
        self.amount = amount
        self.status = status

    def get_transaction_details(self):
        print("Transaction details are:", self.acc_num, self.ifsc_code, self.amount, self.status)


sai = Transaction("1234567890", "ABCD123456", 320.39, True)

sai.get_transaction_details()
