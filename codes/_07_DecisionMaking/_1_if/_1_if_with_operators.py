'''
0 vs None:
-------------
0    - Value
None - Not Applicable

        Marlabs ---> TCS  --> ICICI
        (Payroll)
Employee: Permanent Employee : eid, name, sal
          Contract Employee  : eid, name, None
          Intern             : eid, name, None


'''
'''

if <condition>:
    block of code
'''


# If customer entered value is 100 then print "Congratulations". Else "I am Sorry"
# STATE
cval = int(input("Enter value : "))

# BEHAVIOR
if cval == 100:
    print("Congratulations")
    print("----------------")
else:
    print("I am Sorry")
    print("----------------")





'''
# True ==> non-zero         non None
           -5,6,4.5,-3.6    'M' [1,2] (1,) {1:1,2:2}, {1,2,3}
           
# False ==> 0               None
                            ''  [] () {} {}
'''

if 10:
    print("Value is 10")
if -23:
    print("Value is -23")

if 0:
    print("Value is 0")
if None:
    print("Value is None")
if not None:
    print("Value is not None")

print("---------Sample Programs----------")

print("---------1 Arithmetic----------")

if 10:   # 10 --> Non 0 --> True
    print("Value is 10")

if 10+20:    # 30 -> Non 0 -> True
    print("Arithmetic ops Addition1 ")

if 10-10:    # 0 --> False
    print("Arithmetic ops Substraction 1 ")

if 10-20:
    print("Arithmetic ops Substraction 2")


print("---------2 Comparison/Relational----------")
if 10 > 20:
    print("Comparions ops 1")

if 10+20 > 5+10:
    print("Comparisons ops 2 ")


print("------- 3. Logical Operators--------")
x = True
y = False

if x or y:
    print("Boolean or1")

if False or True:
    print("Boolean or2")

if 10 > 20 or 5 < 10:
    print("Boolean or3")

#  examples of logical operators

print("------- 4. Membership Operators--------")
# Membership
if 'M' in 'Madhu':
    print("Char exists")
# list tuple dict set

print("------- 5. Identity Operators--------")



print("------- 6. Assignment Operators--------")



