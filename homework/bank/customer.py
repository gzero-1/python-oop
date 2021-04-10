from people import People

class Customer(People):
    def __init__(self, name, last):
        #super(Customer, self).__init__(name, last)
        super().__init__(name, last)
        #People.__init__(self, name, last)
