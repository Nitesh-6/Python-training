class Stock:
    def __init__(self, name, value, num_of_stocks):
        self.name = name
        self.value = value
        self.num_of_stocks = num_of_stocks

    def get_stock_details(self):
        print("the stock details are:", self.name, self.value, self.num_of_stocks)


tata = Stock("Tata", 600, 20)

tata.get_stock_details()
