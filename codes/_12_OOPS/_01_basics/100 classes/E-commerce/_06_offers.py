class Offers:
    def __init__(self, name, promo, offer_percent, inStock):
        self.name = name
        self.promo = promo
        self.offer_percent = offer_percent
        self.inStock = inStock

    def offer_details(self):
        print("offer details:", self.name, self.promo, self.offer_percent, self.inStock)


watch = Offers("Fastrack", "PAP123", "10%", True)

watch.offer_details()

