from people import People
from employee import Employee
from customer import Customer

class PeopleManager(object):
    def __init__(self):
        self.people = list()

    @property
    def size(self):
        return len(self.people)

    def add(self, persON):
        if type(person) is not People:
            raise TypeError(f"{type(person)} is not supported")

        self.people.append(person)

    def addEmployee(self, name, last, rol):
        employee = Employee(name, last, rol)
        self.people.append(employee)
        
    def addCustomer(self, name, last):
        customer = Customer(name, last)
        self.people.append(customer)
