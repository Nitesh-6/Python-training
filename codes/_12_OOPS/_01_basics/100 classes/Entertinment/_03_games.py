class Game:
    def __init__(self, name, type, size, num_of_players):
        self.name = name
        self.type = type
        self.size = size
        self.num_of_players = num_of_players

    def game_details(self):
        print("the game is:", self.name, self.type, self.size, self.num_of_players)


bgmi = Game("BGMI", "online", "1.4GB", 100)

bgmi.game_details()
