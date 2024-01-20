class Recipy:
    def __init__(self, name, ingredients, time):
        self.name = name
        self.ingredients = ingredients
        self.time = time

    def get_recirpy(self):
        print("The recipy details are", self.name, self.ingredients, self.time)
    

biryani = Recipy("biryani", "rice", "1.5 hrs")
biryani.get_recirpy()
