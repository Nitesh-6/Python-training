'''
Dictionary:
---------------
word1: meaning
word2: meaning1, meaning2, meaning3

performance: <meaning>

Item ==> key: value

Dictionary Properties***:
========================
- key should be Unique
- key should be Immutable (int,float,bool,str,tuple)     (list,dict,set) XXX
        - value can be anything
'''
stu_ids = [1, 2, 3, 4, 5]
emp_ids = [1, 2, 3, 4, 5]
mobile_bill = [343.23, 456.54, 654.76]

e_info = [100, 'MadhuN', 15000, "Bangalore", "Oracle", "Oracle", "Bangalore"]
order_info = [122, 3, 4234, 232, 123213, "Samsung"]



e_names = []
# 100 employee data  {eid name sal age address} # [{},{},{},{}]

e_data = [50000, 'Madhu Nettem', 45000, 'Male', 'Bangalore', '560037', ['123', 'Marthahalli']]
# address
print("Employee data : ", e_data)

order_details = [12123321, 2133213, 12323, 34, 2, 56, 'SAMSUNG LED TV', 43243, '43242']

e_data = {'eid': 50000,
          'name': 'Madhu Nettem',
          'sal': 50000,
          'gender': 'Male',
          'eid': 123,
          'loc': 'Bangalore',
          'pin': '560037',
          'address': {'hno': '5456', 'main': '23', 'cross': '34', 'block': '342', 'area': 'Marthahalli'}
          }

order_details = {'order_no': 123213,
                 'ref_no': 3432,
                 'cust_name': 'Madhu Nettem',
                 'del_loc': 'Bangalore',
                 'total_bill': 543.56,
                 'discount': 23,
                 'disc_percent': 5,
                 'pin_code': '560037',
                 'no_of_items': 4,
                 }

# Immutable: int float bool string tuple
# Mutable  : list, dict, set

# json format

# UI ---> Python ---> Database
# json    dictionary    record

'''
Normal English Dictionary:
- Can a word be duplicated          ? NO  : Unique, Fixed  => Key  : Unique,Immutable 
- Can a meaning be duplicated       ? Yes : Duplicates     => value: can be anything
- Can a word has 2 or more meanings ? YES : 
'''
# KEY : VALUE
'''
Python Dictionary:
- Can a KEY be duplicated           ? NO  : Unique, Immutable(int,float,bool,str,tuple)
- Can a VALUE be duplicated         ? YES : Duplicates
- Can a KEY has set of values       ? YES : Value can be anything 
'''

'''
Dictionary is Mutable.
Properties of Key:
        1. Dictionary keys must be UNIQUE
        2. Dictionary keys must be IMMUTABLE  (int, float, bool, str, tuple)
                                               list, dict, set -> Mutable 
'''
print("Before : ", e_data)
print("Data  : ", e_data['loc'])
print("House no : ", e_data['address']['hno'])
print("House no : ", e_data['address'])


'''
Map<String,Integer> map = new HashMap<String,Integer>()
map.add('eid',100)

di = {}
di = {'eid':100}

'''
e_data = {'eid': 50000,
          'name': 'Madhu Nettem',
          'sal': 50000,
          'gender': 'Male',
          'eid': 123,
          'loc': 'Bangalore',
          'pin': '560037',
          'address': {'hno': '5456', 'main': '23', 'cross': '34', 'block': '342', 'area': {'zone':'Marthahalli', 'block':3}},
          10: 123455
          }

mob_no = '324324324'  # int(input("Enter mobile no"))
e_data['mobile_no'] = mob_no  # will create new item
e_data['sal'] = 60000         # will update existing key sal
e_data[10] = 345435435
e_data["10"] = 324324
# create list.iterate through

print("After  : ", e_data)

print("Emp sal    :", e_data['eid'])
print("Emp area   : ", e_data['address']['area']['zone'])  # list[2][3]
print("Emp area   : ", e_data['address']['data'][2])


e_data = {'eid': 45000,
          'name': 'Madhu Nettem',
          'sal': 95000,
          'gender': 'Male',
          'eid': 123,
          'loc': 'Bangalore',
          'pin': '560037',
          'address': {'hno': '5456', 'area': 'Marthahalli', 'data': [12, 32, 13, 34]}
          }
print("Emp sal    :", e_data['eid'])
print("Emp sal    :", e_data['address']['hno'])

# e_data['technology']

# [{}, {}, {} .....]

print("----------Dictionary items----------")
for key, val in e_data.items():  #  [('eid', 45000), ('name','Madhu Nettem')]
    print(key, "-----", val)

print("----------Dictionary keys----------")
for key in e_data.keys():  # ['eid','name','sal',....]
    print(key)

print("----------Dictionary values----------")
for val in e_data.values():  # [,,,,]
    print(val)




# UI ---> Python ----> Database
'''
Signup    
-----------
firstname : Madhu
lastname  : Nettem
mobileno  : 7406332332
mailid    : xyz@gmail.com
userid    : xyz
password  : xyz@13
gender    : Male
location  : Bangalore   
# json format *** 

# 100 signup users information  ==> list of dictionaries

user_info = [{'name':'madhu','pass':'123'}, {}, 2,3,4,5....100]

for user in user_info:
    user['pass'] = '456'

user_info = {'udata':[{'name':'madhu','pass':'123'},.......]
             }
'''
# ev_nos = [2,4,6,8,10....]
e_ids = [1, 2, 3, 4, 5, 6, 7]

order_details = [123213, 3432, 'Madhu Nettem', 'Bangalore', 543.56, 23, 5, '560037', 4]

order_details = {'order_no': 123213,
                 'ref_no': 3432,
                 'cust_name': 'Madhu Nettem',
                 'del_loc': 'Bangalore',
                 'total_bill': 543.56,
                 'discount': 23,
                 'disc_percnt': 5,
                 'pin_code': '560037',
                 'no_of_items': 4,
                 }

# order_details[5]
# order_details['discount']

print("Order details : ", order_details)
print("Location : ", order_details['del_loc'])
print("Order No : ", order_details['order_no'])
# print("Order No : ", order_details[100])


'''
Dictionary Properties: 
    - Mutable data structure
    - Unordered
    - Key value pair i.e, item 
    Key properties:
        - Keys must be UNIQUE
        - Keys must be IMMUTABLE 
                     but values can be anything
        
'''
# 1. Keys must be IMMUTABLE and values can be anything
dict1 = {100: 10,
         200: {1: 1, 2: 2},
         102.3: 29,
         True: 'Madhu',
         'Message': [1, 2, 3, 4, 5],
         (1, 2, 3): (1, 2, 3),
         [1, 2, 3]: {1: 1, 2: 2},  # Wrong, List is mutable
         {1: 1, 2: 2}: "Hello",   # Wrong, dict is mutable
         {1, 2, 3}: "Hello"     # Wrong, set is mutable
         }

print("Keys immutable : ", dict1)
# Dict keys should not be List, Dictionary, Set

# 2. Keys must be Unique
x = 10
x = 20

dict1 = {10: 100,
         20: 200,
         10: 150
         }
print("Dictionary: ", dict1)  # {10:150, 20:200}

'''
hash table algoritham
-------------
key    value
-------------
10     150
20     200
'''

list1 = [11, 22, 33]
print(list1)
print(list1[2])


print("Keys must be unique :", dict1)


