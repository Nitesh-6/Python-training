from flask import Flask, request


app = Flask(__name__)

@app.route("/student/create", methods=['POST'])
def create_student():
    print("------------Before loading data------------")
    data = request.get_json()
    print("CONTROLLER : Student Data: ", data)
    return "Success"



if __name__ == '__main__':
    app.run(host='localhost', port=5444)