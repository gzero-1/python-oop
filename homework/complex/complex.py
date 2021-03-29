class ComplexNumber(object):
    ADD = "+"
    SUB = "-"
    MUL = "*"
    def __init__(self, real, imaginary):
        if type(real) is int or type(real) is float:
            self.real = real
        else:
            raise TypeError(f"{type(real)} is not supported") 

        if type(imaginary) is int or type(imaginary) is float:
            self.imaginary = imaginary
        else:
            raise TypeError(f"{type(imaginary)} is not supported") 

    def __str__(self):
        sign = "" if self.imaginary < 0 else "+ "
        return f"{self.real} {sign}{self.imaginary}i"

    def doOperation(self, c, op):
        real = 0
        imaginary = 0

        if type(c) is not ComplexNumber:
            raise TypeError(f"{type(c)} is not supported") 
        elif op == self.ADD:
            real = self.real + c.real
            imaginary = self.imaginary + c.imaginary
        elif op == self.SUB:
            real = self.real - c.real
            imaginary = self.imaginary - c.imaginary
        elif op == self.MUL:
            real = self.real * c.real - self.imaginary * c.imaginary
            imaginary = self.real * c.imaginary + self.imaginary * c.real

        return(ComplexNumber(real, imaginary))

    def __add__(self, c):
        return(self.doOperation(c, self.ADD))

    def __sub__(self, c):
        return(self.doOperation(c, self.SUB))

    def __mul__(self, c):
        return(self.doOperation(c, self.MUL))

