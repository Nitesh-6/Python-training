class Internet_banking:
    def __init__(self, user_name, password, name, bal):
        self.user_name = user_name
        self.password = password
        self.name = name
        self.bal = bal

    def get_details(self):
        print("The account details are:", self.user_name, self.password, self.name, self.bal)


sai = Internet_banking("sainitesh6", "Nitesh@00", "nitesh", 3500.34)

sai.get_details()

