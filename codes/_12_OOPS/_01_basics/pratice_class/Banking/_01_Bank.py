class Bank:
    def __init__(self, name, code, address, branch):
        self.name = name
        self.code = code
        self.address = address
        self.branch = branch

    # Behavior
    def get_data(self):
        print("Bank details:", self.name, self.code, self.address, self.branch)


# object creation
hdfc = Bank("HDFC", "ABC12300", "vizag", "Kommadi")

# method call

hdfc.get_data()
