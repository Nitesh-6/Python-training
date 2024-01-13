''''''

'''
json module:
=============
- Python has a built-in package called json, which can be used to work with JSON data.
- JSON is a syntax for storing and exchanging data.
- JSON is text, written with JavaScript object notation.
- Example : 
    data =  '{ "name":"John", "age":30, "city":"New York"}'

- This package provides all the necessary tools for working with JSON Objects 
  including parsing, serializing, deserializing,
'''
# REQ 1: Convert json to Python object

import json

# Prepare json data
emp = '{"id":"100", "name": "Madhu N", "department" : "Python", "sal" : "10000"}'
print("Json Data : ", emp, type(emp))

print("------ Convert json to Python object ------")
# Convert string to Python dict
emp_dict = json.loads(emp)
print("Python Data : ", emp_dict, type(emp_dict))
