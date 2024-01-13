
# Dictionary is Mutable
# int x = 10
# CREATE

'''
'''
'''
Keys must be unique and immutable
Value can be anything

Signup operation:
===================
FisrtName:  <Dyn data>
LastName :  <Dyn data>
Email    :  <Dyn data>
MobileNo :  <Dyn data>


'''
# CREATE
data = {1: 'One', 2: 'Two', 3: 'Two', 'id': '100'}

# RETRIEVE
print("Dictionary : ", data, type(data))
print("Dict item  :", data[2])
print("Dict item  :", data['id'])

# UPDATE
data[2] = 'Twenty'
data['id'] = 200
print("Dictionary update: ", data)

# DELETE
'''
1. Delete entire  dict   --> del data
2. Delete any one item   --> del data['id']
3. Delete entire items   --> data.clear()
'''

del data[3]
del data['id']
print("Dictionary delete1: ", data)

data.clear()
print("Dictionary delete2: ", data)

data['sal'] = 1000
print("Dictionary delete3: ", data)

# del data
x = 10
print("X : ", x)
del x
# print("X : ",x)

del data
# print("Dictionary delete: ", data) ERROR

'''
Hashing Technique:
==================
A - 1 
B - 2 
C - 3 
D - 4
...
Z - 26

1. Hashcode: 
ABC : 1+2+3 : 6
AC  : 1+3   : 4
AAB : 1+1+2 : 4
AD  : 1+4   : 5
AE  : 1+5   : 6

2. Equal Strings : AC AAB     ABC AE 
                   same hashcode but are they equal  ? NO  

1. hashcode()
2. equals()

                                                            Creation  Retrieval
                                                                        One      All 
Scenario: 10000 elements :  1 element   : 1 bucket : 10000 :  Slower    Faster   Slower
Scenario: 10000 elements :  10000       : 1 bucket : 10000 :  Faster    VerySlow  Faster
Scenario: 10000 elements :  100 element : 1 bucket : 100   :  Faster    Faster    Slower
'''
