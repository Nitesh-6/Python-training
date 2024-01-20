class Activity:
    def __init__(self, activity, type, num_of_ppl, time_req):
        self.activity = activity
        self.type = type
        self.num_of_ppl = num_of_ppl
        self.time_req = time_req

    def get_activity_details(self):
        print("the activity is:", self.activity, self.type, self.num_of_ppl, self.time_req)


dance = Activity("dance", "western", 6, "4:00")

dance.get_activity_details()
