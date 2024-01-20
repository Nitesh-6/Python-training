class Menu:
    def __init__(self, id, name, price, ingredients, qty):
        self.id = id
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.qty = qty

    def get_menu_details(self):
        print("The menu is: ", self.id, self.name, self.price, self.ingredients, self.qty)


biryani = Menu(1, "biryani", 250.0, "rice", "500 gms")
biryani.get_menu_details()
