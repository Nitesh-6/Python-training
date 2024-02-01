# python 2.x vs 3.x   2.7 vs 3.6 7 8 9 10 11

# https://www.geeksforgeeks.org/important-differences-between-python-2-x-and-python-3-x-with-examples/

# Division operator
print(7 / 5)
print(- 7 / 5)

'''
Output in Python 2.x      1    -2
Output in Python 3.x :  1.4   -1.4
'''
# print function

# print 'Hello, Geeks'  # Python 3.x doesn't support

print('Hope You like these facts')

# unicode format   ascii vs unicode
print(type('default string '))
print(type(b'string with b '))
print(b'string with b ')

print(type('default string '))
print(type(u'string with b '))




# 2.x    range   --> Iterator
#        xrange  --> Generator

# 3.x    range   --> Generator

print("======range===========")
for i in range(5):
    print(i)

# Error Handling:
try:
    raise NameError("Name error raised")
except NameError as err:  # NameError,  err
    print(err, 'Error Caused')


    #  Employee emp = new Employee()
    # emp = Employee()