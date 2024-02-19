from flask import Flask, request
from emp_service import save_data
app = Flask(__name__)

# Index Page
@app.route("/")  # endpint : /
def index():
    print("----- This is index page--------")
    return "Hello World, Weclome"

# Signup Page
@app.route("/signup")  # endpint : /signup
def signup_page():
    edata = request.get_json(silent=True)
    print("Data : ", edata)
    print("-------- Request came for sign up --------")
    return "Giving you Signup Page"

# Endpoint for deleting a record
@app.route("/employee/delete/<id>", methods=["DELETE"])
def delete_emp(id):
    print("Deleting employee record: ", id)
    return "Deletion Success"



# Create Employee
@app.route("/employee/create", methods=['POST'])
def create_employee():
    # 1. Load data
    edata = request.get_json()
    print("CONTROLLER : Employee Data : ", edata)
    # 2. Validata data
    edata["loc"] = edata["loc"].capitalize()
    # 3. Pass data to service
    response = save_data(edata)
    print("CONTROLLER : Response is : ", response)
    # 4. Send final response to UI
    print("-------- Request came for emp creation  --------")
    return response



# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    app.run(host='localhost', port=5444)  # host,portno