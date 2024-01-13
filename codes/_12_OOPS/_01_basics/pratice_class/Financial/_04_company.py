class Company:
    def __init__(self, name, stock_value, employees, income):
        self.name = name
        self.stock_value = stock_value
        self.employees = employees
        self.income = income

    def get_company_details(self):
        print("company Details are:", self.name, self.stock_value, self.employees, self.income)


sai = Company("sai", 700.00, 32, "200 cr")

sai.get_company_details()
