class Transport:
    def __init__(self, name, trans_type, charge, duration):
        self.name = name
        self.trans_type = trans_type
        self.charge = charge
        self.duration = duration

    def seller_info(self):
        print("seller information:", self.name, self.trans_type, self.charge, self.duration)


e_kart = Transport("E-kart", "road", 2100.00, "3 hrs")

e_kart.seller_info()