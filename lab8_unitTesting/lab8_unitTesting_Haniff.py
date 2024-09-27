"""
Alisa Haniff
Sept 27, 2024
Unit Testing
"""

import unittest

print(f"\n--------Example #1 simple function unit test 1 file---------\n")
def addTwoNumbers(a,b):
    return a+b

#create a unit tes to check if the function 'addTwoNumbers' is working properly
class TestAddFunction(unittest.TestCase):
    def test_addTwoNumbers(self):
        self.assertEqual(addTwoNumbers(3,5),8)

if __name__ == '__main__':
    unittest.main()

