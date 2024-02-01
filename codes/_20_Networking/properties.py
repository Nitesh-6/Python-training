

# Reusable components across the project
# Paytm module :

# Variables, Constants
COMPANY  = 'PAYTM APPLICATIONS PRIVATE LIMITED'
# Link(Mapping) bank account in paytm
# Fund tranfer
BLINK_URL   = 'http://hdfcbank.com/api/v1/register'
BLINK_METHOD = 'POST'

FT_URL   = 'http://hdfcbank.com/api/v1/fundtransfer'
FT_METHOD = 'POST'

# Functions
# Classess

'''
        1.CUSTOMER   ---> 2.PAYTM      >>> 3.RAMESWARAM     
         CLIENT     ----> SERVER        
         (100 Rs)        
         (0 Rs)
                                    4.HDFC Bank
                                    
                                    

API Call: Web Services***                
                        
Requirement:
------------
- Pay the bill to Coffee Shop from our wallet.



         
BillPayment: 
---------------
10 Rs. 

HDFC Bank: Will expose API end points
*****************************************************         
Link Bank Account: 
====================
    API End point:
    --------------
    Request URL   : http://hdfcbank.com/api/v1/register
    Request Method: POST 
    Payload       : {"account_id":12342343242355,
                     "user_id": 324324,
                     "card_num":23432432432,
                     "name" : "Madhu",
                     "mobile_num": 23432432432,
                     "cvv": 234, 
                     "expiry_date" : 23423432
                     }


Fund Transfer: 
====================
    API End point:
    --------------
    Request URL   : http://hdfcbank.com/api/v1/fundtransfer
    Request Method: POST 
    Payload       : {"account_id":12342343242355,
                     "user_id": 324324,
                     "card_num":23432432432,
                     "name" : "Madhu",
                     "mobile_num": 23432432432
                     }
   
   
Aadhar Registration:
=========================
1. Create Aadhar Card
   Madhu  ---->      BangaloreOne(e-Seva)    ---->       UIDAI 
                        FullName
                        Pancard
                        Address Proof
                        SSC Marks sheet 
                        Finger prints 
                        photo 
                        eye scan
2. Validate Aadhar Card
   Madhu  ---->      Jio    ---->       UIDAI 

            
3. Update details in Aadhar Card:
4. Delete Aadhar Card 
5. Download Aadhar Card

Two ways: 
-------------
   1. Directly access through website UIDAI 
            Client       Server
            -----------------------
            Customer     UIDAI

  2. Go to BangaloreOne(e-Seva)
           
UIDAI Website exposes end points : 
----------------------------------
1. Register Aadhar Card 
2. 
                   
'''