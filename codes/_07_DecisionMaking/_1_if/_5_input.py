''''''
'''
   UI  ---> Backend   ---> Database
==========================================
 HTML       Python          Postgresql 
 CSS        Java            MySQL
 JS         .Net            Oracle
----------------------------------------------------
 10%         100%              50%     : Python 
 10%          70%              100%    : Data Engg.
----------------------------------------------------
 
 userid   (serverside)
 password (client)
   
Validations : Client side : UI Side
              Server side : Backend

Web application:  
        UI   --->   Python/Java/.Net ---> Database
       Basic        Strong                Hands on
       
Static page vs Dynamic page
------------------------------------
1. gmail signup page   : Static
2. gmail login page    : Static
3. gmail home page     : Dynamic
4. gmail sent mail     : Dynamic 
5. paytm login page    : Static
6. paytm my orders     : Dynamic
7. paytm shopping cart : Dynamic


SDLC:   Waterfall / Agile(Scrum***)
-------------------------------------------
1. Requirement Gathering   REQUIREMENT*/Story/Ticket/Incident
2. Analysis
     - Functional
     - Technical
3. Design
4. Development **
5. Testing *
6. Deployment Production


Requirement/Story/Ticket/Incident/Service Request:

1. Requirement Gathering:
==========================
    Requirement: Get Student Result.
         Descr : As an end user, student will give his/her marks as input 
                 and we should give result PASS/FAIL based on his marks.
                 -------------------------------------------------------------
                 State    : Student marks
                 Behavior : Give result PASS/FAIL
                 -------------------------------------------------------------
2. Analysis:
=================
  I. Functional Analysis:
            User Criteria : Input Data: type  : int
                            User Input: Between 0 to 100
            Conditional Data --- Student marks
                                        >= 35 : PASS
                                        < 35  : FAIL
        If marks greater than or equal to  35 then result is PASS
        else if marks are less than 35 then result is FAIL

  II. Technical Analysis:
            a. CRUD       :  Create
            b. STATE      :  Data types/Structures    :   int : marks
            c. Validations:  Between 0 to 100
            c. BEHAVIOR   :  Operators / DM / Loops   :   
                              =  >=  <   DM(if-else)

 III. Design:
            Maths Approach 
            

'''
# IV. Development:
# State
marks = int(input("Enter Marks : "))
print("Student Entered Marks are : ", marks)
# Validation Logic
if marks >= 0 and marks <= 100:      # -10 150   -1 0 1    99 100 101
    print("----Valid Marks----")
    # Behavior
    if marks >= 35:   # 34 35 36 20   70
        print("Result is PASS")
    else:
        print("Result is FAIL")
else:
    print("----Invalid Marks")

if marks >= 0 and marks <= 100:
    pass
    if marks >= 35:
        pass
    else:
        pass
else:
    pass













   # STATE
# marks = 56  # hard coding data
marks = int(input("Enter marks : "))   # 10   "10"   int("10") --> 10

# Validation  # -10  150  23      -1 0 1    99 100 101
if marks >= 0 and marks <= 100:
    print("Valid marks")
    if marks >= 35:    #  60 25    34 35 36
        print("Student result : PASS")
        if marks >= 60:
            print("----- First Class -----")
        elif marks >= 50:
            print("----- Second Class -----")
        else:
            print("----- Third Class -----")
    else:
        print("Student result : FAIL")
else:
    print("Invalid marks")

print("--------------------------------")




'''
    # BEHAVIOR
if marks >= 35:
    print("Result is : PASS")
else:
    print("Result is : FAIL")
print("------------------------------")
'''
'''
# With validations  : Validation --> Business logic

if marks >= 0 and marks <= 100:
    print("---Valid marks---")
    if marks >= 35:
        print("RESULT IS PASS")
    else:
        print("RESULT IS FAIL")
else:
    print("---Invalid marks---")
print("------------------------------------")

# V. Testing
# VI. Production



# Static initialization
x = 10
print("Value of x1: ", x, type(x))

# Dynamic initialization
# x = input()
x = input("Enter value2 : ")  # 100 ==> "100"
print("Value of x2: ", x, type(x))

x = int(input("Enter value3 : "))  # 10 ==> "10" --> 10
print("Value of x3: ", x, type(x))

x = float(input("Enter value3 : "))  # 10.5 ==> "10.5" --> 10.5
print("Value of x3: ", x, type(x))
'''

'''
In Decision Making perspective:
================================
True : True,             Non zero,      Non None
       20>10             30 40 50       "hello"  [1,2,3] 
       1 in {1,2,3}     -23 -45         (1,2,3)  {1:1,2:2}
       True and True                    {1,2,3} 
       True or False   
            
False : False,            Zero           None
        25<10             0              ""  [] 
        10 in {1,2,3}                    ()  {} set({})
        True and False
        False or False
        

0 vs None

Employee:
============
Internship: eid = 100, name = Madhu, sal = None 
Permanent : eid = 100, name = Madhu, sal = 0/1000/10000

1. 50 programs: if conditions with all datatypes/datastructures  and operators
2. 2 Conditions : 
3. 3 Conditions : 
4. Nested Functions  

'''
