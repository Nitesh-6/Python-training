class Doctors:
    def __init__(self, name, age, specialization, salary, experience):
        self.name = name
        self.age = age
        self.specialization = specialization
        self.salary = salary
        self.experience = experience

    def doctor_details(self):
        print("The doctors are:", self.name, self.age, self.specialization, self.salary, self.experience)


sai = Doctors("sai", 24, "skin", 43000.0, "2yrs")
sai.doctor_details()
