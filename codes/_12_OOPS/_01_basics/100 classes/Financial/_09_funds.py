class Funds:
    def __init__(self, id, name, type, return_percent):
        self.id = id
        self.name = name
        self.type = type
        self.return_percent = return_percent

    def get_fund(self):
        print("funds are:", self.id, self.name, self.type, self.return_percent)


sai = Funds(1, "sai", "mutual", "7%")

sai.get_fund()
