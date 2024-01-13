'''
https://www.youtube.com/watch?v=GY6Q2f2kvY0
https://www.youtube.com/watch?v=52tpYl2tTqk
'''

'''
FUNCTIONS:
============  
Given function : f(x) = 2x + 1. Find f(x)    when x = 10 ?
                 -------------  ---------    ------------
    Maths:         Equation      Problem      Input data 
                 -------------  ---------    -------------
    P.L  :        Behavior      REQ/Ticket     State
                     3             1             2

REQ/Ticket  : Find f(x)
    STATE       : x = 10 
    BEHAVIOR    : 2x+1


As given x = 10
Substitute value of 10 in x
    f(x) = 2x+1
After substituting in given expression
    f(10)= 2(10)+1
         = 20+1
         = 21
    f(10) = 21


x = 10

f(x) = 2x + 1

# Python Function 
def f(x):
    result = 2*x+1
    print("Result is : ", result)

# Python Function call 
f(10)
f(10+20)
f(10*2)
a = 5
f(a*a+10)

print(10)  print(10+20)


    
    
f(x) = 2x+1

def f(x): 
    res = 2x+1
    print("Result is : ", res)






Linear Function : f(x) = 2x + 1.
                  Observe behavior** of given function with values from -2 to 2.
 
                                  f(x)  | 2x + 1 
                                    ----------------
                                  f(-2) | 2(-2) + 1    = -4 + 1 = -3   ==> f(-2) = -3
                                  f(-1) | 2(-1) + 1    = -2 + 1 = -1   ==> f(-1) = -1
                                  f(0)  | 2(0)  + 1    =  0 + 1 =  1   ==>  f(0) =  1
                                  f(1)  | 2(1)  + 1    =  2 + 1 =  3   ==>  f(1) =  3
                                  f(2)  | 2(2)  + 1    =  4 + 1 =  5   ==>  f(2) =  5
                                  
                                5 |        #
                                  |
                                4 |  
                                  |                               
                                3 |   #
                                  |
                                2 |
                                  |
                                1 #
                                  |                              
        -*----*----*----*----*----*----*----*----*----*----*--------    
        -5   -4   -3   -2   -1    0    1    2    3    4    5
                                  |
                             # -1 |
                                  |
                               -2 |
                                  |
                        #      -3 |


f(y) = 2x+1
f(f(y)) = 3x+2.
Get output if x = 10

Solution:
--------------
As given 
    f(y) = 2x+1
Given x = 10
    f(y) = 2(10)+1
    f(y) = 20+1
    f(y) = 21

f(f(y)) = f(21) = 3x+2
                = 3(21)+2
                = 63+2
                = 65
                
                
Problem:
-----------
REQ:  Given f(x) = 2x+3. Find g(f(x)) = 3x2+2x+4 when x = 10

1. REQ: Find g(f(x)) = 3x2+2x+4
2. State: x = 10
3. Behavior: f(x) = 2x+3

2 Tasks:
------------
T1. Find f(x) 
T2: Substitute f(x) value in g(f(x))

As given expression f(x) = 2x+3
Given x= 10 
Substitute x value in f(x) expression 
f(10) = 2(10) + 3 
      = 20 + 3
      = 23 
As given expression g(f(x)) = 3x2+2x+4
From above solution f(10) = 23 
Substitute f(10) value in g(f(x)) expression 

g(f(x)) = 3x2+2x+4
g(23)   = 3(23)(23)+2(23)+4 
        = 32323
        

'''

