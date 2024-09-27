"""
Alisa Haniff
Sept 27, 2024
Unit Testing
"""

import unittest


def addTwoNumbers(a,b):
    return a+b

#create a unit tes to check if the function 'addTwoNumbers' is working properly
class TestAddFunction(unittest.TestCase):
    def test_addTwoNumbers(self):
        