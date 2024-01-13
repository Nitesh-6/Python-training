# String is Immutable
msg = 'Hello'
print("Before string : ", msg)
msg = msg + 'World'
print("After string  : ", msg)


# List is Mutable
list1 = [32, 12, 35, 76, 43, 52, 15]
'''       0   1   2   3   4   5   6
          45  46  47  48  49  50  51
        10000
'''


print("Before list :   ", list1, id(list1), id(list1[0]), id(list1[1]), id(list1[2]))
list1[1] = 1000
print("After list  : ", list1, id(list1), id(list1[0]), id(list1[1]), id(list1[2]))
print("After list  : ", list1, id(list1), id(list1[0]), id(list1[1]), id(list1[2]))
list1.insert(1, 22)
print("After list  : ", list1, id(list1), id(list1[0]), id(list1[1]), id(list1[2]))


list1 = [1, 2, 3, 4, 5, 6]
list1[2] = 'hello'