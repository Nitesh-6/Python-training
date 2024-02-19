from flask import Flask
from flask_restful import Api
from emp_controller import Employee

# https://www.geeksforgeeks.org/python-build-a-rest-api-using-flask/
app = Flask(__name__)

api = Api(app)
api.add_resource(Employee, '/api/v1/emp_ops/')

@app.route('/')
def hello():
    print("---------I am hello function. Got request from UI---------")
    return "HELLO WORLD !"


'''
For any API call: 
------------------
Flask will create object of User class    obj = User()
 If request method is GET    : obj.get()
 If request method is POST   : obj.post()
 If request method is PUT    : obj.put()
 If request method is DELETE : obj.delete()


 Monolithic: 
                  UI ---->   flask service    ---> Database
                                |
                                | ----> rest api call --------> ext. other services
                                        requests.get()
                                        requests.post()

 Microservices:
 -------------------
 requests.get()
 requests.post()
                UI  ---->     service1   -----> service2       ----> Database
                                 |                                    |
                                 |--->    service3--------------------> 


                                                        external service
'''

# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    app.run(host='localhost', port=5444)  # host,portno