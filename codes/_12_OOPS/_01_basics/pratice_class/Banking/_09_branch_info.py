class Branch_info:
    def __init__(self, branch_name, location, num_of_emp, num_of_customers):
        self.branch_name = branch_name
        self.location = location
        self.num_of_emp = num_of_emp
        self.num_of_customers = num_of_customers

    def get_branch_info(self):
        print("The branch info:", self.branch_name, self.location, self.num_of_emp, self.num_of_customers)


kommadi = Branch_info("Kommadi", "vizag", 25, 170)

kommadi.get_branch_info()
