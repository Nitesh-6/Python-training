class Customers:
    def __init__(self, cid, account_num, bal, customer_status):
        self.cid = cid
        self.account_num = account_num
        self.bal = bal
        self.customer_status = customer_status

    def get_customer_info(self):
        print("customer details are:", self.cid, self.account_num, self.bal, self.customer_status)


sai = Customers(123, "1234567890", 4312.99, True)

sai.get_customer_info()