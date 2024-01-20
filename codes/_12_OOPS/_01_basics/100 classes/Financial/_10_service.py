class Service:
    def __init__(self, id, type, rating, time):
        self.id = id
        self.type = type
        self.rating = rating
        self.time = time

    def get_service(self):
        print("service provided are:", self.id, self.type, self.rating, self.time)


sai = Service(1, "customer service", 4.5, "15min")

sai.get_service()
