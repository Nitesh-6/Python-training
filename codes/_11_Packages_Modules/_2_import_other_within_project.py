from _10_Functions.get_sum import add
# from package.subpackage.module import function,class,var
# from package.subpackage import module
print("Sum of values : ", add(10, 20))
print("Sum of values : ", add(10, 20))



from _10_Functions import get_sum

print("Sum of values : ", get_sum.add(10, 20))



def gety(p, q):
    print("-----Getting y data ------")
    print("Division result : ", p/q)  # 10/0
    li = [10, 20, 30]
    print("List value : ", li[4])

def getx(a, b):
    print("------Getting x data -------")
    gety(a, b)

def sum1(x,y):
    print("----I am in sum1 function----")
    res = getx(x, y)
    return res

sum1(10, 0)   # Root cause of the issue