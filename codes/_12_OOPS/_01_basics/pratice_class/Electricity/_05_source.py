class Source:
    def __init__(self, name, capacity, price):
        self.name = name
        self.capacity = capacity
        self.price = price

    def source_details(self):
        print("source details:", self.name, self.capacity, self.price)


trans = Source("transformer", "120w", "6/unit")

trans.source_details()
