'''
MVC Architecture
---------------------
Model   View      Controller
         UI
Who will prepare API Call ? UI Developer

'''
'''
REQUIREMENT : Employee onboarding form 

Step1:  API tools : Postman, Insomnia, Swagger
Step2:  Prepare API Call 
            API Call : 
            ----------------
            Request URL    : https://ferilionlabs.com./employee/create 
            Request Method : POST
            Payload        : {
                              "emp_id": 100,
                              "ename": "Madhu Nettem",
                              "mobile": "74069003421",
                              "email": "madhu@ferilionlabs.com",
                              "loc": "Bangalore"
                            } 
            Response: Success : "Created employee successfully"
                      Failure : "Unable to Create"

Step 3: Implement API call(End point)
            1. Configure api in postman tool 
            2. Configure 3 libraries 
                > python -m pip install flask 
                > python -m pip install flask_restful
                > python -m pip install psycopg2
            3. Map api call in backend (In app.py configure then end point)
            4. Implement logic using MVC Architecture


Refer: 
https://stackoverflow.com/questions/62795434/how-to-properly-map-user-defined-methods-to-get-post-http-calls-in-python-flask
'''