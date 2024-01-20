class Bookings:
    def __init__(self, name, date, time, table_num):
        self.name = name
        self.date = date
        self.time = time
        self.table_num = table_num

    def get_booking_details(self):
        print("The booking details are:", self.name, self.date, self.time, self.table_num)


sai = Bookings("sai", "26-01-2024", "13:00", 6)
sai.get_booking_details()
