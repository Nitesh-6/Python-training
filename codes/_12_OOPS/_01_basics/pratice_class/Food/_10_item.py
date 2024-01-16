class Item:
    def __init__(self, name, ingredients, time_to_cook):
        self.name = name
        self.ingredients = ingredients
        self.time_to_cook = time_to_cook

    def get_item_details(self):
        print(f"the item is {self.name}, ingredients are {self.ingredients} time take to cook {self.time_to_cook}")


palav = Item("palav", "Rice", "1.5 hrs")
palav.get_item_details()
