class Travel:
    def __init__(self, source, destination, mode, time_take):
        self.source = source
        self.destination = destination
        self.mode = mode
        self.time_take = time_take

    def get_travel_details(self):
        print("the travel details are:", self.source, self.destination, self.mode, self.time_take)


kurnool = Travel("kurnool", "Vizag", "train", "14 hrs")
kurnool.get_travel_details()
