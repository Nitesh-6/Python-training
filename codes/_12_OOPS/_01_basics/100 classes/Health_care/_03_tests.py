class Test:
    def __init__(self, id, test_name, charge, result):
        self.id = id
        self.test_name = test_name
        self.charge = charge
        self.result = result

    def test_details(self):
        print("The test results are:", self.id, self.test_name, self.charge, self.result)


malaria = Test(1, "Malaria", 180.0, False)
malaria.test_details()
