class Online_service:
    def __init__(self, name, location, rating, num_of_emp):
        self.name = name
        self.location = location
        self.rating = rating
        self.num_of_emp = num_of_emp

    def get_online_ser_details(self):
        print("details are:", self.name, self.location, self.rating, self.num_of_emp)


swiggy = Online_service("swiggy", "vizag", 4.2, 200)
swiggy.get_online_ser_details()
