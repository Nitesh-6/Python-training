x = 10
# li = list(x)  # string tuple range()  # Hello World
# print("List : ", li) Not possible

# Conversions
x = 10
# print(list(x))
print("To float : ", float(x), type(x))
x = 10.5
print("To int  : ", int(x), type(x))
x = 0
print("To bool : ", bool(x), type(x))
x = -5
print("To bool : ", bool(x), type(x))

x = 12345
print("To str  : ", x, type(x))
x = str(x)
print("To str  : ", x, type(x))

print("List of nums : ", list(x))  # ['1','2','3','4','5']

str1 = 'Hello World'
print("Convert to list : ", list(str1))  # ['H','e','l',,,,,]


list1 = [1, 2, 3, 4, 5, 6]
# print("Join on numbers : ", ''.join(list1))
print("List to string : ", list1, type(list1))
st = str(list1)
print("List to string : ", st, type(st))  # "[1, 2, 3, 4, 5, 6]"
'''
[1, 2, 3,  4 ,  5 ,   6]   # 123456
012345678910 11 121314 15
'''
list1 = ['1', '2', '3', '4', '5', '6']  # "123456"    "123456"
num_str = ''.join(list1)   # ''+'1'  '1'+'2' ==>  '123456'
print(num_str, type(num_str))
num_str = ' '.join(list1)
print(num_str, type(num_str))
num_str = '*'.join(list1)
print(num_str, type(num_str))
