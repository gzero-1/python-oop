import pytest
from complex import ComplexNumber 

def test_add():
    c1 = ComplexNumber(1,2)
    c2 = ComplexNumber(3,4)
    result = c1 + c2
    assert str(result) == "4 + 6i"
    print(result)

def test_mul():
    c1 = ComplexNumber(1,2)
    c2 = ComplexNumber(3,4)
    result = c1 * c2
    assert str(result) == "-5 + 10i"
    print(result)

def test_raise_TypeError_str():
    with pytest.raises(TypeError):
        c1 = ComplexNumber("1","2")

def test_raise_TypeError_array():
    with pytest.raises(TypeError):
        c1 = ComplexNumber([1],[2])

