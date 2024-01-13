# Scope of variable  LEGB Rule in python  non-local

x = 100  # Global scope
print("Value of x1 :", x)

def get_data():
    # print("Value of x2 :", x)
    a = 10  # local scope
    x = 25  # local scope
    print("Value of x3 :", x, a)

get_data()
print("Function Details : ", get_data)
print("Value of x4 :", x)
# print("Value of x4 :", a)  # ERROR

