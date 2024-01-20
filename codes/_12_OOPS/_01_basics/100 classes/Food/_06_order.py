class Orders:
    def __init__(self, id, name, price, is_paid):
        self.id = id
        self.name = name
        self.price = price
        self.is_paid = is_paid

    def get_order_details(self):
        return f"Order ID: {self.id}, Name: {self.name}, Price: {self.price}, is_paid: {self.is_paid}"
    
biryani = Orders(6, "Biryani", 250.0, True)
print(biryani.get_order_details())