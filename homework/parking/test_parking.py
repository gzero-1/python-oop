from parking import Parking
from car import Car



p = Parking()
#p.cars = [Car(1), Car(2), Car(3)]
#for car in p.cars:
#    p.add_time(1)
#    p.car_out(car)
car1 = Car()
car2 = Car()
p.add_time(2)
car1.came_in(p)
p.add_time(4)
car2.came_in(p)
car1.came_out(p)
p.add_time(1)
car2.came_out(p)





