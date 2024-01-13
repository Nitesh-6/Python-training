class Chef:
    def __init__(self, name, id, special_dish, salary, experience):
        self.name = name
        self.id = id
        self.special_dish = special_dish
        self.salary = salary
        self.experience = experience

    def get_chef_details(self):
        print("Chef details are: ", self.name, self.id, self.special_dish, self.salary, self.experience)

sai = Chef("Nitesh", 6, "biryani", 23000.0, "3 years")

sai.get_chef_details()