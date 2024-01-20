class Money_transefer:
    def __init__(self, name, acc_no, amount, reciver_accno):
        self.name = name
        self.acc_no = acc_no
        self.amount = amount
        self.reciver_accno = reciver_accno

    def transaction(self):
        print("Transaction Details:", self.name, self.acc_no, self.amount, self.reciver_accno)


nitesh = Money_transefer("nitesh", "0123456789", 210.01, "12334567890")

nitesh.transaction()
