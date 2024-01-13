  # Lambda function or Ananymous Function

# REQ: Find Square of given value.

      # 1mark : Find square of given value 5

print("Square of value : ", 5 ** 2)

       # 2 mark : Find square of given value 5
val = 5
sq = val ** 2
print("Square of value : ", sq)

# 5 marks : Find square of given value 5

val = int(input("Enter value : "))

def find_square(num):
    res = num ** 2
    return res

out = find_square(val)
print("Square of value : ", out)

# 10 marks : Find square of given value 5

class SquareVal:
    def __init__(self, val):
        self.val = val

    def get_square(self):
        res = self.val ** 2
        return res

obj = SquareVal(5)
sq = obj.get_square()
print("Square value is : ", sq)

# 20 marks Question
# User proper exception handling, load value from file : file handling

# OR

print("Square of value : ", find_square(val))

'''
sq_val = num * num
return sq_val
'''


'''
Syntax: lambda parameters: expression
'''
def find_square(num):
    return num ** 2

# Lambda or Ananymous function

sq_val = lambda num: num ** 2
print("Square of value : ", sq_val(5))




sq_val = lambda num: num ** 2
print("Lambda  : Square of value : ", sq_val(10))


sq_val = lambda x, y: x * y
print("Lambda  : Square of value : ", sq_val(10, 20))


# Covert to function
def sq_val(x, y):
    return x*y

print("Function : Square of value : ", sq_val(5,10))

# Use lambda functions  ==> map filter reduce functions
# https://www.geeksforgeeks.org/python-lambda-anonymous-functions-filter-map-reduce/
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def get_squares(li):
    li2 = []
    for val in li:
        li2.append(val ** 2)

get_squares(list1)


# 1. Lambda with map:
print("--------Lambda with map-------")
li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

res = map(lambda x: x**2, li)  # <map object at 0x000002AE8B35B9D0>
print("Map :: Square of values :  ", res)
res = list(map(lambda x: x**2, li))
print("Map :: Square of values :  ", res)




# 2. Lambda with filter:
print("--------Lambda with filter-------")

li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]

# Using Regular Function
def filter_list(li1):
    li2 = []
    for val in li1:
        if val % 2 == 0:
            li2.append(val)
    return li2
print("Functions: Even numbers1: ", filter_list(li))


res = filter(lambda x: x % 2 == 0, li)   # 22 54 62 ...
print("Filter :: Even Numbers :  ", res)  # filter object
res = list(filter(lambda x: x % 2 == 0, li))
print("Filter :: Even Numbers :  ", res)   # list of even numbers

# 3. Lambda with reduce:
# REQ: Addition of list of values

'''
    O1: = 5+8+10+20+50+100
    O2: = 13+10+20+50+100
        = 23+20+50+100
        = 43+50+100
        = 93+100
        = 193


'''
from functools import reduce
print("--------Lambda with reduce-------")

li = [5, 8, 10, 20, 50, 100]   # 13 + 10

res = reduce(lambda x, y: x+y, li)  # 193
print("Reduce : Get Addition of list :  ", res)



x = 'Hello'
print("Value   : ", x)
print("Address : ", id(x))
print("Type    : ", type(x))