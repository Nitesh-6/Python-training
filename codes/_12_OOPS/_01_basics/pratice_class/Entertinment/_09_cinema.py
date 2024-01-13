class Movie:
    def __init__(self, name, hero, duration, relese_date):
        self.name = name
        self.hero = hero
        self.duration = duration
        self.relese_date = relese_date

    def get_movie_details(self):
        print("Movie details are:", self.name, self.hero, self.duration, self.relese_date)


salaar = Movie("Salaar", "prabhas", "3:00 hrs", "22-12-2023")

salaar.get_movie_details()
