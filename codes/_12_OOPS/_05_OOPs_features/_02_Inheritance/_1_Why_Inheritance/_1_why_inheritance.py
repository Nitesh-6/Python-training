'''
Inheritance : is - a   **: - Square is a Polygon
Aggregation : has - a    : - Square has 4 sides


 - Employee has eid
 - Employee has name
 - Employee has salary
 - Employee has address
'''
'''
has - a : Aggregation:

Web Application:   UI   --->        Python            ----> Database 
                            Controller Service DAO

Controller : Load data from UI, do server side validations
Service    : Implement business logic 
DAO        : Perform db operations  
'''


class Address:

    def __init__(self, hno, city, pincode):
        self.hno = hno
        self.city = city
        self.pincode = pincode

    def get_address(self):
        return self.hno + " , " + self.city + " , " + self.pincode



class Employee:
    def __init__(self, eid: int, name: str, sal: float, addr: Address):
        self.eid = eid
        self.name = name
        self.sal = sal
        self.addr = addr  # User Defined Class
    def get_einfo(self):
        print("Employee Info :", self.eid, self.name, self.sal, self.addr.get_address())

address = Address('100', 'Banaglore', '560036')
madhu = Employee(123, 'Madhu Nettem', 15000, address)
madhu.get_einfo()
'''
is - a : Inheritance:
=======================
Parent
Children

Square is a Quadrilateral 

Parent / Base / Super Class   : Quadrilateral
Child  / Derived /  Sub Class : Square 



is-a relationship    <SUB> is a <SUPER>
SoftwareEmployee is a Animal 

2 classes: 
    Super   - Sub* 
    Parent  - Child* 
    Base    - Derived 

madhu = Employee() 
    madhu = Physical 
    Employee = Logical 

Problem:             Tiger    Lion        Cat         Dog 
                       eating()   eating()   eating()    eating()
                            
                            Problem - Code Duplication
    
                        Animal 
                          eating()
                            Problem - We should not generalize
                    
    
Solution:                 Animal
                            eating()
               |      |           |     |
              Tiger  Lion        Cat    Dog      A5 A6 A7 A8 ......


A3:                        Animal
                  |                   |
                Wild               Domestic
                |  |                 |     |
             Tiger Lion              Cat   Dog 
    
    

Without inheritance:
---------------------
Tiger, Lion, Cat, Dog 

A1:    Tiger        Lion              Cat         Dog 
        eating()    eating()           eating()   eating()   
  
  # Code duplication, Maintenance, Enhancements

With inheritance:
---------------------
A2:                   Animal
        Tiger   Lion         Cat    Dog 
    
                       Animal
                         eating()         # code reusability, avoids code duplication
             |        |           |       |  
         Tiger        Lion        Cat     Dog   
      
Inheritance => is-a relationship **
Aggregation => has-a relationship  # Controller - Service - DAO layer
# aggregation vs composition vs association
Tiger is a Animal     - TRUE
Lion is a Animal      - TRUE
Cat is a Animal       - TRUE
Dog is a Animal       - TRUE
SEmployee is a Animal - FALSE 

        FileWriter
pdf excel ppt word  csv txt

LED TV is a TV
LCD TV is a TV
Laptop is a TV

SOLID Principles :  
--------------------
S - Single Responsibility Principle**
O - Open-Closed**
L - Liskov Substitution
I - Interface Segregation
D - Dependency Inversion**

'''

