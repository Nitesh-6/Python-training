class Holyday:
    def __init__(self, destination, source, num_of_ppl, num_ofDays):
        self.destination = destination
        self.source = source
        self.num_of_ppl = num_of_ppl
        self.num_of_days = num_ofDays

    def holyday_details(self):
        print("the holyday details are:", self.destination, self.source, self.num_of_ppl, self.num_of_days)


araku = Holyday("araku", "vizag", 6, 4)

araku.holyday_details()
