''''''
'''
                                      Code %
Projects :  Development /            60%-100%
            Enhancement(Release) /    40-60%
            Production Support        10-30%
                        (AMS, PS, Support, Maintenance)

# GIT       : Branching Strategies 
                - main 
                    - development 
                        - 1233_Get einfo (feature branch)
                        - 1234_Update Address
                        ......
Commands : git clone "branchname"
           git checkout -branchname 
           After code changes in local system 
                - Push code to feature branch 
                        - git status 
                        - git diff 
                        - git add       
                        - git commit 
                        - git push 
                        
# Instances : Local, DEV, TEST/QA/Staging, UAT, PRODUCTION
                1     2         3           4       5
 
 Web Application:
 -------------------
      json               psycopg2
 UI   ---->   Backend     ----> Database 
               CSD
                
Layers:  Loose Coupling 
--------
Controller: Receives request from UI, Server Validations 
Service   : Business Logic 
DAO       : Database CRUD Operations 
'''
'''
SDLC Stages:
-------------
Requirement Gathering
Analysis - Functional/Technical
Design   - Sequence Diagrams(UML Diagrams)
Development
Testing
Deployment(Production)
'''

print("Start of program")
num = 1
while num <= 10:   # Each iteration
    print("Number : ", num)
    num += 1
print("End of program")


class Employee:
    pass



# Remove all even numbers in list
list1 = [1, 12, 10, 22, 44, 3, 34, 10, 5, 66, 6, 10, 7, 88, 18, 9, 100]
     # #[1, 10, 22, 44, 3, 34, 10, 5, 66, 6, 10, 7, 88, 18, 9, 100]

print("Before list  :", list1)
for val in list1:
    if val % 2 == 0:
        list1.remove(val)      # [1,10,22,44....]
print("After list   :", list1)
print("----------------------------------")
print("Before list  :", list1)
li2 = []
for val in list1:
    if val % 2 == 0:
        li2.append(val)
print("To be removed :", li2)
print("After list   :", list1)




'''
Project Types : DEV Enhancement ProductionSupport
Environments  : Local, DEV, TEST, UAT, PRODUCTION 
--------------------------------------------------
Production issue occurance : Live environment / Production environment
Issue will be reported by customer 
Ticket to developer 
 - Replicate(reproduce) the issue 
        - Able to replicate
            - 1.1 Root cause analysis (Find what is the reason for issue) # DEBUGGING
            - 1.2 Fix the issue
            - 1.3 Testing  (Local, DEV, Test, UAT ) instances
            - 1.4 Deploy to production instance 
        - Not able to replicate
            - Production Logs 
            
'''


def get_data(x):
    print("Data is : ", x)
    print("Hello world")
    den = x-10
    return 10/den

def getinfo(val):
    print("I am in info")
    res = get_data(val)
    print("Result is : ", res)

print("Before method call")
v = 10  # int(input("Enter value : "))
getinfo(v)
print("After method call")