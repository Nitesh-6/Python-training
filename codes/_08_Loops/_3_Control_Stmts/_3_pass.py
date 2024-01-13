''''''
'''
"pass" can be used in all blocks 
    - if elif else 
    - while for 
    - function
    - class  
    - try except else finally 
    - with

Case 1 : Skeleton structure
Case 2 : We are not able to understand req.
Case 3 : Requirement specification is pending from Client 
'''

# Case 1 : Skeleton structure
# REQ: I need student division. Generally
#       >= 35 pass <35 fail
#       if marks >= 60 1st class, >= 50 2nd class, >= 35 Third Class

marks = 56

if marks >= 0 and marks <= 100:
    pass
    if marks >= 35:
        pass
        if marks >= 60:
            pass
        elif marks >= 50:
            pass
        else:
            pass
    else:
        pass
else:
    pass


# Case 2 : We are not able to understand req.
# REQ: I need student division. Generally if marks >= 60 1st class, >= 50 2nd class, >= 35 Third Class

marks = 100

if marks >= 0 and marks <= 100:
    print("---Valid Marks----")
    if marks >= 35:
        print("----PASS---")
        if marks >= 60:
            pass
        elif marks >= 50:
            pass
        else:
            pass
    else:
        print("---FAIL---")
else:
    print("---Invalid marks---")


# Case 3 : Requirement is pending from client side
# REQ: I need student division. >= 35 pass <35 fail. Generally for division if marks >= 60 >= 50 >= 35.

marks = 100

if marks >= 0 and marks <= 100:
    print("---Valid Marks----")
    if marks >= 35:
        print("----PASS---")
        if marks >= 60:
            pass
        elif marks >= 50:
            pass
        else:
            pass
    else:
        print("---FAIL---")
else:
    print("---Invalid marks---")




'''
if marks >= 90:
    pass
elif marks >= 80:
    pass
elif marks >= 70:
    pass 
elif marks >= 60:
    pass
elif marks >= 50:
    pass 

if marks >= 90:
    # 20 lines 
elif marks >= 80:
    # 40 lines 
elif marks >= 70:
    # 40 lines 
    
    
if rating == 5:
    # 5 lines
elif rating == 4:
    pass
elif rating == 3:
    pass
elif rating == 2:
    pass
elif rating == 1:
    pass
elif rating == 0:
    pass

'''




# Case 1: Print numbers between 1 to 100. And if num is divisible by 5  then
# work on rest api calls for integration of services.

''
for val in range(1, 101):
    if val % 5 == 0:
        pass
    print("Value : ", val)


# Case 1: Print numbers between 1 to 100. And if num is divisible by 5 then.

''
for val in range(1, 101):
    if val % 5 == 0:
        pass
    print("Value : ", val)



# Print numbers between 1  to 10.
# IF val is 2 => condition   3=> condition .... 10 => conditinos

for val in range(1, 10):
    if val == 2:
        pass
    elif val == 3:
        pass
    elif val == 4:
        pass
    elif val == 10:
        pass


for val in range(1, 101):
    if val % 5 == 0:
        pass
    print(val)
'''
if
elif
elif
elif
elif
elif
elif
elif <condition>:
    pass
elif <condition>:
    pass
elif <condition>:
    pass
'''







# given number positive print it as IS, negative print as is, elif 0 <some action>

num1 = int(input("Enter numbeer"))

if num1 > 0:
    print("Positive value is : ", num1)
elif num1 < 0:
    print("Negative value is : ", num1)
else:
    pass




# pass can be used in all blocks
'''
if 
elif 
else 
while 
for 
function blocks 
class 
file handling 
exception handling
'''
# Print  first 6 numbers which are divisible by 6 between 1 to 100
# If number ends with 0 don't display it

count = 0
for val in range(1, 101):
    if val % 6 == 0:
        count += 1
        if val % 10 == 0:
            continue
        print(val)
        if count == 6:
            break
print("--End of loop----")

# $@#Q$dasfdsf#@#$#@EDSF

# Validations
# Client side validations
# Server side validations
