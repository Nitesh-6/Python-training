
from _11_Packages_Modules.xyz.test1 import get_data
from test1 import name, get_data, Employee
from _10_Functions._10_Scope import x

def print_data():
    res = get_data()
    return res


print("Printing data : ", print_data())