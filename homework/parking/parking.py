class Parking:
    price = 10

    def __init__(self):
        self.__timer = 0

    def add_time(self, time):
        self.__timer += time

    def car_in(self):
       return self.__timer

    def car_out(self, check_in_time):
        total_time = self.__timer - check_in_time
        bill = f"car came in at: {check_in_time}" 
        bill += f"\ngot out at: {self.__timer}"
        bill += f"\nTotal time was: {total_time}"
        bill += f"\nPaid:{total_time * self.price}"

        print("\n--------------------")
        print(bill)
