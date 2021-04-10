from people import People
from rol import Rol

class Employee(People):
    def __init__(self, name, last, rol):
        super().__init__(name, last)
        if type(rol) is not Rol:
            raise TypeError(f"{type(rol)} is not supported as Rol")
        self.rol = rol
