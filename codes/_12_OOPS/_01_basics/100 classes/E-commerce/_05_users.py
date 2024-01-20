class Users:
    def __init__(self, uid, password, address, phone):
        self.uid = uid
        self.password = password
        self.address = address
        self.phone = phone

    def user_data(self):
        print("user details:", self.uid, self.password, self.address, self.phone)


sai = Users("sai99", "nitesh@111", "vizag", 8919065372)

sai.user_data()
