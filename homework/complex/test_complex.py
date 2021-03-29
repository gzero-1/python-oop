import unittest
from complex import ComplexNumber 

class TestComplex(unittest.TestCase):
    def setUp(self):
        self.c1 = ComplexNumber(1,2)
        self.c2 = ComplexNumber(3,4)

    def test_add(self):
        result = self.c1 + self.c2
        self.assertEqual(str(result), "4 + 6i")
        print(result)
        result = self.c2 + self.c1
        self.assertEqual(str(result), "4 + 6i")
        print(result)

    def test_mul(self):
        result = self.c1 * self.c2
        self.assertEqual(str(result), "-5 + 10i")
        print(result)
        result = self.c2 * self.c1
        self.assertEqual(str(result), "-5 + 10i")
        print(result)

    def test_raise_TypeError_str(self):
        self.assertRaises(TypeError, ComplexNumber,"1", "2")

    def test_raise_TypeError_array(self):
        with self.assertRaises(TypeError):
            c1 = ComplexNumber([1],[2])


if __name__ == "__main__":
    unittest.main()
