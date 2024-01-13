''''''
'''
Data structures : State     - NOUN
Function        : Behavior  - Verb/Adverb  CRUD

Entity: Employee
------------------
    STATE :  Data types/Structures
            Attributes: empid, name, sal, address, mobile, email
                        100, Madhu, 15000, Bangalore, 324324324, email@gmail.com
                        int,str,float,str,str,str
    BEHAVIOR : CRUD
            - Create Employee
            - Retrieve Employee
            - Update Employee mobileno
            - Delete Employee



x = 10    # State
print(x)  # Behavior

print()  : prints the given content
id()     :
type()   :

int() float() complex()
bool()

str() 40+
list() 10+
tuple() 2+
dict() 10+
set() 3+



'''
#include<stdio.h> prinf scanf

# builtins.py
# Function calling/Invocation
print("Hello World")

# REQ: Adding 2 numbers
'''
STATE    : 2 Numbers 
BEHAVIOR : Adding
'''
       # I. STATE : Customer input
num1 = int(input("Enter number 1 :"))  # 10  Static way
num2 = int(input("Enter number 2 :"))  # 20  Static way
       # II. BEHAVIOR: Business Logic
result = num1 + num2
# III. Give response to user
print("Addition is : ", result)


print(10, 20)
print("------------")
'''
Maths Functions:
-------------------
 - Behavior of function will get changed based on input value 
 - Define function only one time, reuse it n no of times
 
'''

'''
# Find sum of 2 given numbers
--------------------------------
STATE    ==> I.  ==> 10,20  
BEHAVIOR ==> II, III. Perform addition and give result 

STATE:
--------
       # I. Customer input
num1 = int(input("Enter number 1 :"))
num2 = int(input("Enter number 2 :"))

BEHAVIOR:
----------
       # II. Business Logic
result = num1 + num2
       # III. Give response to user
print("Addition is : ",result)


# FUNCTIONS
Advantages: - Avoids code duplication ==> Achieves Code reusability
            - When enhancements are required, 
                        we need "code changes" in only one place 

# Functions:
----------------
REQ:  f(x) = 2x2+3x+1. Find the value of f(x)   when x is 10
      ---------------  ----------------------   ------------
       3. BEHAVIOR       1. REQUIREMENT            2. STATE
       
As given x = 10  # STATE
Given expression is 
        f(x) = 2x2+3x+1  # BEHAVIOR
   Substitute the value 10 in x in given above expression
f(10) = 2(10*10)+3(10)+1
      = 2(100)+30+1
      = 200+30+1
f(10) = 231       # RESULT / Output

Find the behavior  of f(x) when x value ranges from -2 to 2

# Function Definition:
-----------------------
    f(x)  = 2x2+3x+1   
     
# Function calling:
-----------------------
f(-2) = 2(-2*-2)+3(-2)+1  = 3
f(-1) = 2(-1*-1)+3(-1)+1  = 0
f(0)  = 2(0*0)+3(0)+1  	  =	1
f(1)  = 2(1*1)+3(1)+1     = 6
f(2)  = 2(2*2)+3(2)+1     = 15
f(10) = 2(10*10)+3(10)+1  = 231


# Function Definition:
-----------------------
    f(x, y)  = 2xy+3x+4y+1 

# Function Calling:
-----------------------
    f(2, 3)  = 2(2)(3)+ 3(2) + 4(3) + 1
             = 12 + 6 + 12 + 1
             = 31
              




Maths:              P.L
------------------------------------------------------------
f(x) = 2x2+3x+1    # Function definition (Signature, Body)
                        def f(x):
                           result = 2*x**2+3*x+1
                         
f(10)              # Function calling by passing value
                           f(10)  
2(10**2)+3(10)+1   # Function execution
                            result = 2*10**2+3*10+1
231                # Function end result 
                            result = 231
                            
                            
f(x) = 2x2+3x+1

    # Function Definition
def f(x):
    res = 2*x*x+3*x+1
    print("Result is :", res)


    # Function Calling 
f(10)
f(20)
f(-4)
.........
'''

def f(x):
    result = 2*x*x + 3*x + 1
    print("Result is : ", result)

f(10)
f(20)
f(30)

# Sum of 2 numbers

# State
num1 = 10
num2 = 20

# Behavior : Function Definition
def add(n1, n2):     # def add(int n1, int n2):
    result = n1 + n2
    print("Addition is : ", result)

# Function calling
add(num1, num2)
add(5, 15)
add(-10, -20)
add(10+20, 5+15)  # add(30, 5+15)  add(30, 20)
add([1, 2, 3], [4, 5, 6])
add(10, "Hello")


# Behavior

def add_nums(n1, n2):
    result = n1 + n2
    print("Addition is : ", result)


add_nums(num1, num2)
add_nums(5, 7)







# II. Solution with functions
print("II. Addition using functions")

print("--------1. Function for Addition----------")
    # I. STATE
num1 = int(input("Enter number 1 :"))   # 1. Customer input
num2 = int(input("Enter number 2 :"))

    # II. BEHAVIOR
          # 2. Business Logic
          # 3. Give response to user

def add(n1, n2):
    result = n1 + n2
    print("Addition is : ", result)

add(num1, num2)
# num1, num2 arguments
add(-10, -20)
add(10, 20)       # 10,20 arguments
add(0, -20)
add(-20, 0)
add(0, 10)
add(10, 0)
add(0, 0)
add(10+20, 40+50)

print(10)
print(10+20)

x = 10
x = 10+20


# Practice functions for all arithmetic ops

print("--------2. Function for Subtraction----------")


print("--------3. Function for Multiplication----------")

# State
n1 = 10
n2 = 20

# Behavior
def multiply(num1, num2):
    result = num1 * num2
    print("Mulitplication is  : ", result)

# Function call
multiply(n1, n2)
multiply(1, 2)
multiply(2, 5)

print("--------4. Function for Division----------")


print("--------4. Function for Power----------")

# Write functions for all operators: ASSIGNMENT

print("---------II. Comparison Operators")

print("----1. Greater---------")
x = 10
y = 20

def find_greaterval(a, b):
    if a > b:
        print(a, " is greater than ", b)
    else:
        print(b, " is greater than ", a)


find_greaterval(x, y)
find_greaterval(-10, -20)
find_greaterval(-10+20, -20+5)
