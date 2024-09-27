"""Alisa Haniff
Test Employee"""


import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    def setUp(self):
        emp1 = Employee("Peter","Pan", 50000)
        
    def test_emailEmployee(self):
        self.assertEqual(emp1.emailEmployee, "PeterPan@email.com")

    def test_fullname(self):
        emp1 = Employee("Peter","Pan", 50000)
        self.assertEqual(emp1.fullname, "Pan, Peter")
    
    
    
if __name__=="__main__":
    unittest.main()
    