class Singleton(object):
    _instance = None
    def __init__(self):
        print(f"INIT")
        for attr, value in self.__dict__.items():
            print(f"{attr} = {value}")
        self.name = "none"

    def __new__(cls):
        print(cls)
        if cls._instance is None:
            print("NEW")
            cls._instance = super(Singleton, cls).__new__(cls)
        print("before return instance")
        return cls._instance

s1 = Singleton()
s1.name = "ggg"
s2 = Singleton()
print(s1)
print(s2)
print(f"s1.name: {s1.name}, s2.name: {s2.name}")
