class Payment:
    def __init__(self, price, type, platform, pid):
        self.price = price
        self.type = type
        self.platform = platform
        self.pid = pid

    def payment_details(self):
        print("payment type:", self.price, self.type, self.platform, self.pid)


paytm = Payment(200, "online", "paytm", 123)

paytm.payment_details()