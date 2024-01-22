'''
                       Animal
                         eating()         # code reusability, avoids code duplication
             |        |           |       |
         Tiger        Lion        Cat     Dog
'''
class Animal:

    def __init__(self):
        print("SUPER :: Animal constructor")

    def eating(self):
        print("SUPER :: Animal : eating")

class Tiger(Animal):   # Inheritance    Tiger is-a Animal

    def __init__(self):
        print("SUB  :: Tiger constructor")

    def sleeping(self):
        print("SUB  :: Tiger Sleeping")

# Write Lion, Cat, Dog classes and call methods


print("--------super class object creation--------")
anim = Animal()
anim.eating()
# anim.sleeping()  # ERROR

print("--------sub class object creation--------")
tiger = Tiger()   # Tiger tiger = new Tiger()  int x = 10
tiger.sleeping()  # sub class specific method
tiger.eating()    # inherited super class method
# tiger.roaring()  # ERROR
