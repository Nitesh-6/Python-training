class Employee:
    def __init__(self, id, name, exp, phone):
        self.name = name
        self.id = id
        self.exp = exp
        self.phone = phone

    def emp_details(self):
        print("Employee details are:", self.id, self.name, self.exp, self.phone)


sai = Employee(6, "sai", "fresher", "8919065372")
sai.emp_details()