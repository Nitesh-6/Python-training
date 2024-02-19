

'''
        Client                   Server
        --------------------------------
LUDO GAME:
    UI ---> Python ---> Database

In server I am deploying  project :
    - Python Code, UI Code, Database

        Ludo_Project
            - UICode
            - Backend
            - Database

www.ludo.com : Login Page
             : Home Page
             : Game done

            Client                Server
            Laptop   -----------> LudoApp                Banks (50)
            Mobile                                        HDFC    Axis
                                    Python                Java     .Net
                                    Windows               Linux     Mac
API Call:
    - Request URL    : end point
    - Request Method : GET POST PUT DELETE
    - Payload        : Data (State)  UI/Database
   http://hdfc.com/cust_validation
For fund transfer purpose
        - Expose APIs
            1. CustValidation : /cust_validation  (request url/ endpoint*/suffix url)
            2. GetAccountInfo : /get_accinfo
            3. UpdateAccDetails : /update_accdetails
            4. DeleteAccount : /del_acc
            5. FundTranfer
            6. OtpValidation

1. CustValidation:
---------------------
RETRIEVE :
API Call:
    1. Request URL   : https://hdfcbank.com/cust_validation
    2. Request Method: GET
    3. Payload       : {"acc_no":12345,
                        "name":"Madhu",
                        "ifsc": 234324,
                        "expirydate": Date,
                        "cvv" : 232,
                        "location" : "Bangalore"
                        }
Frameworks:
--------------
        UI ----> Python ----> Database

Flask/Django:
From UI : if end point is '/cust_validation' send payload to the mapped function.


Student record:
------------------
API calls will be prepared by UI developers only.

API : Create Student marks:
------------------------------
Request URL   : ./student/create
Request Method: POST
Payload       : {
                    "s_id": 100,
                    "sname": "Madhu Nettem",
                    "marks": 56
                }

# Pay the bill through Paytm:
-------------------------------
1. Open paytm app
2. Open scanner
3. Scan QR Code
4. Check merchant name
5. Enter amount to transfer
6. Select Bank Account
7. Fund Transfer
8. Validate otp
9. Funds will be transferred
10. Confirmation message

FrontEnd       Backend(Paytm Server)
-------------------------------------------
Mobile         Python Code       Database
                C   S    D
                Python Code                    AXIS    HDFC    ICICI    Kotak
                                                Java    .Net    Python   PHP
1 2 3
4. API Call
5. 10 Rs.  6. Selected Bank Account   7. "Insufficient Funds"

Communication Should happen using API call.

    Paytm -------------> Axis Bank
    Python                     Java
          API Call: Web Service*
                                - SOAP
                                - RESTful ***


Simcard:
------------
1. Go to Vendor office Jio
2. Select mobile number
3. Registration
        - Validate Aadhar Card Number
                - Aadhar#, Fingerprint

        Client  --->  Jio        ----> UIDAI
                       C S D    WebService


Web Services:
------------------
- RMI
- SOAP  : only xml
- REST* : supports all formats
        : json format

    Client      Server
    User   ---> Paytm -------> HDFCBank
                                    Expose APIs:
                                    - Link Bank Account
                                    - Fund Transfer
                                    - Check min balance
                                    - Delink Bank Account

BankAccount linking:  REST API CALL to HDFC Bank

                    Ludo                  HDFCBank
                    Client  --REST API CALL--->   Server

                - 1. Send all bank details to Bank
                - 2. Send OTP
Postgresql

UI ---> Python  --> Database

         Paytm                HDFCBank
          (Python)                (Java)
                              ICICI 
                                  (.Net)
        
Web Services : To communicate from one service to other service 
               without any platform dependency issues
             : Communication: API Call (Web service)
             : SOAP / REST**



        

API Call :
============
1. Request URL
2. Request Method
3. Payload

WebService:
-----------
Service1      to Service2  communication
--------         ---------------------------
Python              Java
Windows,            Linux

API Call: Web Service
                - SOAP API Call
                - REST API Call **

User    ---  Paytm    --- Bank 

HTTP Request methods: GET POST PUT (PATCH) DELETE
                      OPTIONS HEAD TRACE

                      GET VS POST
                      POST vs PUT
                      PUT vs PATCH *


SimCard:
------------

    Kishore  --->  AClient --->    AServer   --->   UIDAI

Step1:
---------
    - Aadhar Card
    - Thumb Impression




https://app.exchangerate-api.com/dashboard/confirmed
https://reqres.in



Client                      Server                 Third Party:
==========================================================================
Kishore                  (this module)          https://reqres.in (RHS)
Mobile,Laptop             Paytm,Ludo                  HDFCBank    (database)
ESevaUI                   ESevaServer                 UIDAI       (database)
AirtelOfficeUI            AirtelServer                UIDAI


Kishore+(this module) both are in Server
https://reqres.in     is the third party

API Calls:
----------
1. List Users:
------------------------
GET: Request URL    : https://reqres.in/api/users?page=2
     Request Method : GET
'''
import requests

# Consuming API Call(Third Party) / Calling API
data = requests.get("https://reqres.in/api/users?page=2")
print("DATA : ", data)
print("DATA : ", data.json())
print("----------END of GET ----------------")

'''
2. Get Single User 
====================
API  Call : 
Request URL : https://reqres.in/api/users/2
Request Method: GET 
'''
sdata = requests.get("https://reqres.in/api/users/2")
print("Single User : ", sdata.json())
print("----------END of GET ----------------")


import requests
from utilities import REQRES_URL, HDFC_URL
'''
# 1. List Users
REST API Call: 
        Request URL   : "/api/users?page=2"
        Request Method: GET 
'''


# CREATE USER
'''
API CALL : 
Request URL   : https://reqres.in/api/users 
Request Method: POST  
Payload       : {"name": "morpheus",
                 "job": "leader"
                }
'''
rurl = "https://reqres.in/api/users"
idata = {"name": "Madhu",
        "job": "Nettem"
       }

response = requests.post(url=rurl, data=idata)
print("CREATE Response : ", response.json())
print("----------END of POST ----------------")


