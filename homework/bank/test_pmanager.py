import unittest
from people_manager import PeopleManager
from rol import Rol

class TestPManager(unittest.TestCase):
    def setUp(self):
        self.pm = PeopleManager()

    def test_addEmployee(self):
        self.pm.addEmployee("pedro", "perez", Rol.Manager)
        self.assertEqual(self.pm.size, 1) 

    def test_addEmployee_TypeError(self):
        with self.assertRaises(TypeError):
            self.pm.addEmployee("pedro", "perez", "none")

    def test_addCustomer(self):
        self.pm.addCustomer("pedro", "perez")
        self.assertEqual(self.pm.size, 1) 

if __name__ == "__main__":
    unittest.main() 
