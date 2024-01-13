class Restaurant:
    def __init__(self, name, address, price, item):
        self.name = name
        self.address = address
        self.price = price
        self.item = item

    def get_restaurant_details(self):
        print("the details are:", self.name, self.address, self.price, self.item)


sai = Restaurant("sai", "vizag", 249.00, "Biryani")
sai.get_restaurant_details()


def fizz_buzz(n):
    for i in range(0, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


num = 15
fizz_buzz(num)

