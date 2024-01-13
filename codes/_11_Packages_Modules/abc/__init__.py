import json

my_data = '{"name":"sai", "age":24, "city":"vizag"}'
print("data in json", my_data)
data = json.loads(my_data)

print("data after converting to python", data)
data["age"] = 23
data["name"] = "nitesh"


jsData = json.dumps(data)

print("the data again after converting to json", jsData)

