class Party:
    def __init__(self, type, num_ppl, location, date):
        self.type = type
        self.num_ppl = num_ppl
        self.location = location
        self.date = date

    def get_party_details(self):
        print("party details:", self.type, self.num_ppl, self.location, self.date)


house = Party("House", 20, "vizag", "31-12-2023")

house.get_party_details()
