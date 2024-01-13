# class creation
class Student:
    # state or a constructor
    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks

    # Behaviour
    def get_studentData(self):
        print("Student Information", self.roll, self.name, self.marks)

    def update_marks(self, val):
        self.marks = val

    def get_result(self):
        if self.marks >= 35:
            print("Result: Pass:", self.name)
        else:
            print("Result: Fail:", self.name)

x = 10
# creating an object
sai = Student(6, 'sai nitesh', 70)

nitesh = Student(3, "Nitesh", 75)

# printing all the fields of object sai
sai.get_studentData()

# printing all the fields of object nitesh
nitesh.get_studentData()

# updating the marks of sai
sai.update_marks(77)

# printing all the fields of object sai after updating marks
sai.get_studentData()

# printing the result of nitesh
nitesh.get_result()

# updating the marks of nitesh and getting result
nitesh.update_marks(33)
nitesh.get_result()
