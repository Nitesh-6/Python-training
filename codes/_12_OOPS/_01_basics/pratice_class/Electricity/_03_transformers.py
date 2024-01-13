class Transformers:
    def __init__(self, id, location, capacity, range):
        self.id = id
        self.location = location
        self.capacity = capacity
        self.range = range

    def transformer_details(self):
        print("transformer details are:", self.id, self.location, self.capacity, self.range)


vizag = Transformers(123, "vizag", "20000KW", "1000m")
vizag.transformer_details()
