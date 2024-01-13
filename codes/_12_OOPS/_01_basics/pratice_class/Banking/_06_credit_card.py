class Credit_card:
    def __init__(self, name, card_num, cvv, limit):
        self.name =name
        self.card_num = card_num
        self.cvv =cvv
        self.limit = limit

    def get_card_info(self):
        print("card details are:", self.name, self.card_num, self.cvv, self.limit)


nitesh = Credit_card("nitesh", "123456789012", "000", 25000.00)
nitesh.get_card_info()

