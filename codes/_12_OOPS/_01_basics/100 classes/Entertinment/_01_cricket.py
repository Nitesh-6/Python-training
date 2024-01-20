class Cricket:
    def __init__(self, team, captian, total_score, runrate):
        self.team = team
        self.captian = captian
        self.total_score = total_score
        self.runrate = runrate

    def match_details(self):
        print("Team Details:", self.team, self.captian, self.total_score, self.runrate)


india = Cricket("India", "Rohit Sharma", "350/6", 7.00)

india.match_details()
