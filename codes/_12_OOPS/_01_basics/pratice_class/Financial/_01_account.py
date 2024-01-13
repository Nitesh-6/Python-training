class Account:
    def __init__(self, id, acc_type, name, bal):
        self.id = id
        self.acc_type = acc_type
        self.name = name
        self.bal = bal

    def get_acc_info(self):
        print("the account information:", self.id, self.acc_type, self.name, self.bal)


sai = Account(6, "salary", "sai", 2300.09)

sai.get_acc_info()
