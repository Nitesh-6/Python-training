class Employee:
    def __init__(self, eid, name, age, sal):
        self.eid = eid
        self.name = name
        self.age = age
        self.sal = sal

    def get_employee_details(self):
        print("Employee Details:", self.eid, self.name, self.age, self.sal)


nitesh = Employee(6, "nitesh", 24, 23000.00)

nitesh.get_employee_details()
