

from flask_restful import Resource, request

class Employee(Resource):
    def get(self):
        print("---------Get Employee data ---------")
        return "Emp data Sent"

    def post(self):
        udata = request.get_json()
        print("-----------Store Employee data----------", udata)
        eid = udata["eid"]
        name = udata["name"]
        salary = udata["sal"]
        mobile = udata["mobile"]
        # server side validations
        print("-----------Post method-----------")
        print("Customer Data : ", eid, name, salary, mobile)

        #self.response["status"] = 201
        # self.response["message"] = "User created successfully"
        # return self.response, 201

        return "Success POST"

    def put(self):
        pass

    def delete(self):
        pass

# Inheritance :  Resource res = Employee()



