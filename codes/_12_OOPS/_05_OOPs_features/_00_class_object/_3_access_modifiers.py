class Employee:
    office = 'ORACLE'
    _x = 'XXX'
    __y = "YYY"

    def __init__(self):
        pass

    def get_einfo(self):  # public method
        print("Emp : Public Method")

    def _getinfo(self):  # protected method
        print("Emp : Protected Method")

    def __getinfo(self):  # private method
        print("Emp : Private Method")

print("Employee :", Employee.office)  # public
print("Employee :", Employee._x)      # protected
# print("Employee :", Employee.__y)     # private

obj = Employee()
print("Employee info1 : ", obj.office)
print("Employee info1 : ", obj._x)
# print("Employee info1 : ",obj.__y)

obj = Employee()
print("Employee info1 : ", getattr(obj, "office"))
print("Employee info1 : ", getattr(obj, "_x"))
# print("Employee info1 : ",getattr(obj, "__y"))


obj = Employee()
obj.get_einfo()
obj._getinfo()
# obj.__getinfo()

# enabling functions include type(), isinstance(), callable(), dir() and getattr()
