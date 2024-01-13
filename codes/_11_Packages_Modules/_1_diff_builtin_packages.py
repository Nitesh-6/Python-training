import builtins
'''
builtins.py
---------------
# STATE  : builtin data types  -- classes in
#             numbers (int float  complex)
#             string list tuple dict set

# Behavior : functions id() input() len() max() min()
#                      print()  type()
#                      int() float() long() str() list() tuple() dict() set()
'''
list1 = [1, 2, 3, 4]
list1 = list([1, 2, 3, 4])
print(list1, type(list1), id(list1))
x = 10
list1.append(10)
print(list1, type(list1), id(list1))

# REQ : Generate a random number between 1 to 100

'''
Description: From random.py module import randint function
'''
from random import randint

print("Random number : ", randint(100, 200))
print("-------------------------------------")

'''
Import random module
REQ: Randomly choose a letter from all the ascii_letters
'''
from random import randint, choice, SystemRandom

print("Random number :", randint(100, 200))
print("Choice value :", choice([1, 2, 3, 4, 5, 6]))
print("-------------------------------------")



from random import randint
# 2000 lines
print("Random number :", randint(100, 200))

# OR

import random
# 2000 lines
print("Random number :", random.randint(100, 200))


# print("Random number : ", random('A', 'Z'))

# Function definition exists in random.py module
# randint(1,100) : function call








