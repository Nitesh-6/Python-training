class Fixed_Deposit:
    def __init__(self, name, acc_num, phone, amt_deposited):
        self.name = name
        self.acc_num = acc_num
        self.phone = phone
        self.amt_deposited = amt_deposited

    def get_deposit_info(self):
        print("deposit details:", self.name, self.acc_num, self.phone, self.amt_deposited)


nitesh = Fixed_Deposit("nitesh", "123456789", 8919065372, 1000000.00)
nitesh.get_deposit_info()
