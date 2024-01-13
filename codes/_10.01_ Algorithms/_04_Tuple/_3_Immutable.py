x = 10
del x
'''
Immutability:
    - Use AS IS 
    - Delete it completely
'''
t1 = (1, 2, 3, 4, 5)
# t1[2] = 10  # ERROR : Tuple is Immutable
# del t1[2]
del t1

t1 = (12, 12, 43, [4, 5, 6], 7)  # list dictionary set
# t1[3] = 100 # ERROR
print("Before -- ", t1)
# t1[3] = [7,8,9]
t1[3].append(100)  # YES : It works
# Try with : extend pop remove insert
print("=====>", t1[:-1])
print("After --  ", t1)
# del t1[3]
del t1

t1 = (1)
print(t1, type(t1))
t1 = (1,)
print(t1, type(t1))


list1 = [1, 2, 3, (4, 5, 6), 7, 8, 9]

