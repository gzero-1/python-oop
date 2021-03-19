from list import List

class Lenner:
    @staticmethod
    def lenn(obj):
        len = 0
        if type(obj) is str or type(obj) is list or type(obj) is dict or type(obj) is List:
            for item in obj:
                len += 1
        else:
            raise TypeError(f"{type(obj)} is not supported")
        return len


print(Lenner.lenn("hola"))
print(Lenner.lenn([0,0,22]))
print(Lenner.lenn({'a':"a", 'b':"b"}))
print(Lenner.lenn(List(1,2,3,2,1)))
print(Lenner.lenn(123))
