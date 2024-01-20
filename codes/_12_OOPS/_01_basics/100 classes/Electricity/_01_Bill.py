
class Bill:
    def __init__(self, id, name, location, price):
        self.id = id
        self.name = name
        self.location = location
        self.price = price

    def bill_details(self):
        print("bill details:", self.id, self.name, self.location, self.price)


sai = Bill(123, "sai", "vizag", 123.94)

sai.bill_details()
