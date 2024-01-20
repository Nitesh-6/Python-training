class Concerts:
    def __init__(self, preformer, venue, price, date):
        self.performer = preformer
        self.venue = venue
        self.price = price
        self.date = date

    def get_concert_details(self):
        print("concert details are:", self.performer, self.venue, self.price, self.date)


vizag = Concerts("Anurag", "kommadi", 350.00, "31-12-2023")

vizag.get_concert_details()
