# # REQ: Print customer given number : No conditions
# """
#
# 1. Entity  : Number
# 2. State   : Datatypes/DataStructures: int/float
# 3. Behavior
#         Validations : number or not
#         Operation(CRUD): CREATE
#
#     State: Customer given number
#     Behavior: Print it
#
#  Functional analysis
#  -------------------
#  1. customer will give number : state
#  2. check if it is number or float : Behavior
#  3. if value == number ==> print
#
#  Technical analysis:
#  ------------------
#  1. 1. STATE    :  Datatypes/Datastructures   : Customer given number   (NOUN)  : int
#   2. BEHAVIOR :  Operators, DM, Loops       : Check if it is number or not   (VERB)
#                     NA    NA   NA
#
# """
#
# # STATE
#
# num = int(input("Enter number : "))
# # BEHAVIOR
# print("Number is  :", num)
#
# # 1. print the age if it is greater than or equal to 18
#
# """
# 1. Entity: number
# 2. state: Datatypes/DataStructure: int
# 3. Behavior:
#         validations: age >= 18
#         Operations: create
#
#     state: given age
#     Behavior: print
#
#      Functional analysis
#  -------------------
#  1. customer will give number : state
#  2. check if it is int : Behavior
#  3. if value >= 18 ==> print
#
#  Technical analysis:
#  ------------------
#  1. 1. STATE    :  Datatypes/Datastructures   : Customer given number   (NOUN)  : int
#   2. BEHAVIOR :  Operators, DM, Loops       : Check if it is greater than or equal to 18    (VERB)
#                     > =     if   NA
# """
# # state
#
# age = int(input("Enter a age: "))
#
# # Behavior
#
# if age >= 18:
#     print("Age you entered: ", age)
# print("---code ended---")
#
# # 2. print a number which is divisible by 5
#
# """
# Entity: number
# State: Datatypes/Datastructure = int/float
# Behavior:
#         validation: number should divisible by 5
#         operations: create
#
# state: given number
# Behavior: print
#
#  Functional analysis
#  -------------------
#  1. customer will give number : state
#  2. check if it is number or float : Behavior
#  3. if value divisible by 5 ==> print
#
#  Technical analysis:
#  ------------------
#  1. 1. STATE    :  Datatypes/Datastructures   : Customer given number   (NOUN)  : int
#   2. BEHAVIOR :  Operators, DM,   Loops       : Check if number % 5 ==0 it is divisible by 5   (VERB)
#                   %  =      if    NA
#
# """
#
# number = int(input("Enter a number: "))
#
# if number % 5 == 0:
#     print(number, "is divisible by 5")
#
# print("---code ended---")
#
# # 3. print the number either even or odd
#
# """
# Entity: Number
# State:  Datatypes/Datastructure = int/float
# Behaviour:
#         validations: check it is even or odd
#         operations: create
# Functional analysis :
# -------------------
# 1. customer will give a number : state
# 2. check weather it is int / float: Behavior
# 3. If the value is even or odd: print
# Technical analysis:
# ------------------
# State: Datatype/datastructure : customer given a number : int
# Behavior: operator,    DM,    Loops   : check weather number % 2 == 0 then even else odd
#            % =     if else     NA
#
# """
# num = int(input("Enter a number:"))
#
# if num % 2 == 0:
#     print(num, "is an even number")
# else:
#     print(num, "is an odd number")
#
# print("---code ended---")
#
# # 4. check which one is greater between two numbers
#
# '''
# functional analysis:
# -------------------
# 1. customer will give two numbers : state
# 2. check if it is number id int / float : Behavior
# 3. find which number is greater : print
#
# Technical analysis:
# ------------------
# state : Datatype/dataStructure: int/ float : noun
# Behavior: operator,  DM,   Loops : check a>b and b>a print which is greater
#             >      if elif else  NA
# '''
#
# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter a number: "))
#
# if num1 > num2:
#     print(num1, "is greater than", num2)
# elif num2 > num1:
#     print(num2, "is greater than", num1)
# else:
#     print("both are equal")
#
# # 5. print Check whether entered year is leap year or not.


# arr = [1, 2, 3, 4, 6, 4, 7, 4]
occurrence = int(input("Enter a number to find number of occurrence: "))
arr = input("Enter a values to find number of occurrence: ")
arr = list(arr)
count = 0

for i in arr:
    if int(i) == occurrence:
        count += 1
print(f"The count of {occurrence} in the list is {count}")
print("---code ended---", "\n\n")
