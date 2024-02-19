# Consume this api call in my application
from utilities import REQRES_URL
import requests

end_url = "/api/users?page=2"  # suffix url or end point or end url
# REST API Call
req_url = REQRES_URL + end_url
response = requests.get(req_url)
print("All Users Data :", response.json())

print("-------------------------------------------")
'''
# 2. Single User
'''

'''
# 7. Create User     
=======================
REST API Call: 
        Request URL   : "/api/users"
        Request Method: POST
        Payload       : {
                         "name": "morpheus",
                         "job": "leader"
                        } 
'''
end_url = "/api/users"
req_url = REQRES_URL + end_url
udata = {"name": "Madhu",
            "job": "Software Engg."
          }
response = requests.post(url=req_url, data=udata)
print("Create User statuscode: ", response.status_code)
print("Create User output    : ", response.json())

'''
url = "https://reqres.in/api/users"
info = {"name": "Madhu", "job": "Nettem"}
response = requests.post("https://reqres.in/api/users", data=info)
print("Create User ! : ", response)
print("Create User ! :", response.json())
'''