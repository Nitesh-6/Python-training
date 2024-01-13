class Account:
    def __init__(self, name, address, account_type, phone):
        self.name = name
        self.address = address
        self.account_type = account_type
        self.phone = phone

    def get_account_details(self):
        print("Account Details:", self.name, self.address, self.account_type, self.phone)


nitesh = Account("nitesh", "vizag", "savings", 8919065372)

nitesh.get_account_details()
