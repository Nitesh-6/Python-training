
from dao import save_student

def create_student(data):
    print("SERVICE : Getting Data : ", data)
    resp = save_student(data)
    return resp