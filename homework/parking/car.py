class Car:
    def __init__(self):
        self.__check_in_time = 0
    
    def came_in(self, p):
        self.__check_in_time = p.car_in()

    def came_out(self, p):
        p.car_out(self.__check_in_time)

