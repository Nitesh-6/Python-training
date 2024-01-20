class Cart:
    def __init__(self, quantity, cart_value, name, price):
        self.quantity = quantity
        self.cart_value = cart_value
        self.name = name
        self.price = price

    def cart_val(self):
        print("cart details:", self.quantity, self.cart_value, self.name, self.price)


shirt = Cart(3, 2900.00, "shirt", 1500.00)

shirt.cart_val()
